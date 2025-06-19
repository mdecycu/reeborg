class Harvest:
    def __init__(self, x1, y1, x2, y2):
        # 決定起點與終點的 X、Y 範圍
        self.x_min = min(x1, x2)
        self.x_max = max(x1, x2)
        self.y_min = min(y1, y2)
        self.y_max = max(y1, y2)

    def turn_left_n(self, n):
        for _ in range(n):
            turn_left()
    
    def move_n(self, n):
        for _ in range(n):
            move()
    
    def harvest_one_cell(self):
        while object_here():
            take()
    
    def harvest_one_row(self, cells):
        for _ in range(cells):
            self.harvest_one_cell()
            if _ < cells - 1:
                move()
    
    def move_to_field(self):
        # 假設 Reeborg 起始在 (1,1)，面向東
        self.move_n(self.x_min - 1)
        self.turn_left_n(1)
        self.move_n(self.y_min - 1)
        self.turn_left_n(3) # 轉回向東
    
    def harvest_field(self):
        rows = self.y_max - self.y_min + 1
        cols = self.x_max - self.x_min + 1
        self.move_to_field()
        for r in range(rows):
            self.harvest_one_row(cols)
            if r < rows - 1:
                if r % 2 == 0:
                    self.turn_left_n(1)
                    move()
                    self.turn_left_n(1)
                else:
                    self.turn_left_n(3)
                    move()
                    self.turn_left_n(3)
        # 結束時 Reeborg 面向原來方向

# 使用方式
# 例如, 要採收(3,3)到(8,8)的區域:
h = Harvest(3, 3, 8, 8)
h.harvest_field()