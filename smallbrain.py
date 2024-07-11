class Cerebellum:
    """
    소뇌: 운동 제어와 관련된 작업을 처리하는 역할
    """
    def _init_(self):
        from moving import moving
        self.move = moving()
