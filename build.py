"""Bundle Classroom AI Studio into one offline HTML file."""
import base64, pathlib, sys

ROOT = pathlib.Path(__file__).parent
DEPS = pathlib.Path(sys.argv[1])
src = (ROOT / "src" / "studio.html").read_text(encoding="utf-8")

fonts = DEPS / "fontsource-atkinson-hyperlegible-5.3.0" / "package" / "files"
def face(weight):
    data = base64.b64encode((fonts / f"atkinson-hyperlegible-latin-{weight}-normal.woff2").read_bytes()).decode()
    return ("@font-face{font-family:\"AtkinsonHL\";font-style:normal;font-weight:%d;font-display:swap;"
            "src:url(data:font/woff2;base64,%s) format(\"woff2\")}" % (weight, data))
font_css = face(400) + "\n" + face(700)

pdf = DEPS / "pdfjs-dist-3.11.174" / "package" / "build"
lib = (pdf / "pdf.min.js").read_text(encoding="utf-8")
worker = (pdf / "pdf.worker.min.js").read_text(encoding="utf-8")
for name, code in (("pdf.min.js", lib), ("pdf.worker.min.js", worker)):
    if "</script" in code.lower():
        sys.exit(f"{name} contains a closing script tag; cannot inline safely")

out = (src.replace("/*FONT_CSS*/", font_css)
          .replace("<!--PDFJS-->", "<script>/* PDF.js 3.11.174 (Apache-2.0) */\n" + lib + "\n</script>")
          .replace("<!--PDFWORKER-->", '<script type="text/js-worker" id="pdfjs-worker">' + worker + "</script>"))
assert "/*FONT_CSS*/" not in out and "<!--PDFJS-->" not in out and "<!--PDFWORKER-->" not in out
dist = ROOT / "dist"; dist.mkdir(exist_ok=True)
target = dist / "classroom-ai-studio.html"
target.write_text(out, encoding="utf-8")
print(f"wrote {target} ({target.stat().st_size/1e6:.2f} MB)")
