from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = "super-secret-key-change-me"

# Simulasi Database sederhana
# Flag berada pada ID 0 yang seharusnya 'tersembunyi'
notes = {
    "0": {"title": "FLAG", "content": "RAVEN{ID0R_1s_St1ll_4l1v3_2026}", "author": "admin", "private": True},
    "1": {"title": "Belanja", "content": "Beli kopi dan susu.", "author": "user123", "private": False},
    "2": {"title": "Tugas", "content": "Kerjakan laporan Arsitektur Komputer.", "author": "user123", "private": False}
}

@app.route('/')
def index():
    # Menampilkan daftar catatan publik (ID 1 dan 2)
    public_notes = {k: v for k, v in notes.items() if not v['private']}
    return render_template('index.html', notes=public_notes)

@app.route('/view/<note_id>')
def view_note(note_id):
    note = notes.get(note_id)
    if note:
        return f"<h1>{note['title']}</h1><p>{note['content']}</p><hr><a href='/'>Back</a>"
    return "Note not found!", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)