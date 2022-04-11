import tensorflow as tf
import os

class RL_QG_agent:
    def __init__(self):
        self.model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Reversi")

    def init_model(self):

        # 定义自己的 网络
        self.sess = tf.Session()
        self.saver = tf.train.Saver()
        # 补全代码


    def place(self,state,enables):
        return 123456789

    def save_model(self):  # 保存 模型
        self.saver.save(self.sess, os.path.join(self.model_dir, 'parameter.ckpt'))

    def load_model(self):# 重新导入模型
        self.saver.restore(self.sess, os.path.join(self.model_dir, 'parameter.ckpt'))

    # 定义自己需要的函数