import subprocess, sys

def git(*args):
    return subprocess.run(["git",*args],capture_output=True,text=True,check=False).stdout.strip()

def main():
    before=sys.argv[1] if len(sys.argv)>1 else ""
    after=sys.argv[2] if len(sys.argv)>2 else "HEAD"
    if not before or set(before)=={"0"}:
        paths=git("ls-tree","-r","--name-only",after,"--","submission").splitlines()
    else:
        paths=git("diff","--name-only","--diff-filter=AM",before,after,"--","submission").splitlines()
    exts=(".ipynb",".py",".txt",".md",".csv",".json",".html",".pdf",".docx",".xlsx",".zip")
    for p in paths:
        if p.lower().endswith(exts): print(p)

if __name__=="__main__": main()
