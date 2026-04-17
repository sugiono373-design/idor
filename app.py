from flask import Flask, render_template, os

app = Flask(__name__)
app.secret_key = "super-secret-key-change-me"

# Database simulasi
notes = {
    "0": {"title": "FLAG", "content": "RAVEN{ID0R_1s_St1ll_4l1v3_2026}", "author": "admin", "private": True},
    "1": {"title": "Belanja", "content": "Beli kopi dan susu.", "author": "user123", "private": False},
    "2": {"title": "Tugas", "content": "Kerjakan laporan Arsitektur Komputer.", "author": "user123", "private": False}
}

@app.route('/')
def index():
    # Mengambil note yang tidak private
    public_notes = {k: v for k, v in notes.items() if not v['private']}
    return render_template('index.html', notes=public_notes)

@app.route('/view/<note_id>')
def view_note(note_id):
    note = notes.get(note_id)
    if note:
        # Menghapus spasi aneh dan menggunakan f-string bersih
        return f"""
        <body style="background:#0a0a0a; color:#00ff41; font-family:monospace; padding:50px; text-align:center;">
            <div style="border:1px solid #333; display:inline-block; padding:30px; border-radius:10px;">
                <h1 style="border-bottom:1px solid #333; padding-bottom:10px;">{note['title']}</h1>
                <p style="font-size:1.2em; margin:20px 0;">{note['content']}</p>
                <hr style="border:0; border-top:1px solid #333;">
                <br>
                <a href="/" style="color:#aaa; text-decoration:none;">[ Back to Home ]</a>
            </div>
        </body>
        """
    return "Note not found!", 404

# Jalankan aplikasi (Hanya untuk lokal, Railway pakai Gunicorn)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
