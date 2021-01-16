import math

node_list = []
'''
概要：ノード数取得関数
引数：なし
戻り値：ノード数
'''
def get_node_num(node_list):
    return len(node_list)


'''
概要：初期化関数
引数：なし
戻り値：なし
'''

def init():
    node_list = [[0, 5, 10, 0, 0], [0, 0, 3, 2, 0], [0, 0, 0, 4, 2], [0, 0, 0, 0, 3], [0, 0, 0, 0, 0]]
    nodeNum = get_node_num(node_list)
    unvisitedNode = list(range(nodeNum))
    distans = [math.inf] * nodeNum
    print(distans)
    distans[0] = 0 #初期位置は0
    
    
if __name__ == "__main__":
    init()
