from timer import Timer
from jupiter_flys import generate_seed, jupiter_flys
from generateid import generate_id

passwords = [generate_id(8) for _ in range(1000)]

timer = Timer()
timer.start()
for password in passwords:
    seed = generate_seed(password)
    hashed = jupiter_flys(seed, password)
timer.stop()
