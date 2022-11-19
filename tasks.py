from invoke import task

@task
def start(ctx):
    ctx.run("uvicorn app.main:app --reload")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest app")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task(coverage_report)
def view_report(ctx):
    ctx.run('firefox htmlcov/index.html')

@task
def test(ctx):
    ctx.run("pytest app")

@task
def autopep(ctx):
    ctx.run('autopep8 --in-place --recursive app')

@task
def pylint(ctx):
    ctx.run("pylint app")


