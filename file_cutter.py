import logging.handlers

log = logging.getLogger()
fh = logging.handlers.RotatingFileHandler(
    "tsplit.txt",
    maxBytes=2**20*10,
    backupCount=100
)
# 100 MB each, up to a maximum of 100 files
log.addHandler(fh)
log.setLevel(logging.INFO)
f = open("t1.txt")
while True:
    log.info(f.readline().strip())
