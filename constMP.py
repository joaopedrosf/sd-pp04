#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.37.210','172.31.37.220','172.31.35.253','172.31.39.69','172.31.47.39']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
#PEERS_SAME_REGION = ['54.197.227.5', '34.199.145.45', '44.208.215.62', '44.212.136.6', '52.203.188.224']
PEERS_SAME_REGION = ['34.199.145.45', '44.208.215.62', '44.212.136.6', '54.197.227.5', '3.80.249.252']

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ['54.197.227.5', '34.199.145.45', '44.208.215.62', '54.184.178.236', '44.228.155.68']


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 5   # Number of peers
SERVER_ADDR ='34.239.4.132'
SERVER_PORT = 5678

# Number of valid operations to call
NUM_OPS = 3

# List of operations
ops = ['deposit', 'interest', 'withdraw']

# Ranges of values
depositRange = [1, 10]
interestRange = [1, 2]
withdrawRange = [1, 5]
