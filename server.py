#!/usr/bin/env python3
"""Run:  python server.py   ->  open http://localhost:8000
Serves machine-lab.html and stores all machines in machines.db (SQLite) next to this file."""
import http.server, json, sqlite3, os
D = os.path.dirname(os.path.abspath(__file__)); DBF = os.path.join(D, 'machines.db')
def db():
    c = sqlite3.connect(DBF)
    c.execute('create table if not exists machines(id text primary key, name text, pos integer, data text)')
    c.execute('create table if not exists settings(k text primary key, v text)')
    return c
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=D, **k)
    def js(s, t):
        b = t.encode(); s.send_response(200); s.send_header('Content-Type', 'application/json; charset=utf-8')
        s.send_header('Content-Length', str(len(b))); s.end_headers(); s.wfile.write(b)
    def do_GET(s):
        if s.path == '/api/state':
            c = db(); rows = c.execute('select data from machines order by pos').fetchall()
            cur = c.execute("select v from settings where k='cur'").fetchone(); c.close()
            s.js(json.dumps({'list': [json.loads(r[0]) for r in rows], 'cur': cur[0] if cur else None}) if rows else '{}')
        else:
            if s.path in ('/', ''): s.path = '/machine-lab.html'
            super().do_GET()
    def do_PUT(s):
        if s.path != '/api/state': return s.send_error(404)
        d = json.loads(s.rfile.read(int(s.headers['Content-Length'])))
        c = db(); c.execute('delete from machines')
        for i, m in enumerate(d.get('list', [])):
            c.execute('insert into machines values(?,?,?,?)', (m['id'], m['name'], i, json.dumps(m, ensure_ascii=False)))
        c.execute("insert or replace into settings values('cur',?)", (d.get('cur'),)); c.commit(); c.close(); s.js('{"ok":true}')
print('Open http://localhost:8000   (database: %s)' % DBF)
http.server.ThreadingHTTPServer(('127.0.0.1', 8000), H).serve_forever()
