#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import  unittest

class Student(object):
      def __init__(self,name,score):
        self.name = name
        self.score = score

      def getGrade(self):
         if self.score >= 80 and self.score <90:
             return 'B'
         if self.score >=90 and self.score <= 100:
             return  "A"
         if self.score <0:
            return  "False"
         return  'C'

class testStudent(unittest.TestCase):
      def test_90_to_100(self):
                s1 = Student('Bart',90)
                s2 = Student('Daivd',100)
                self.assertEqual(s1.getGrade(),'A')
                self.assertEqual(s2.getGrade(),"A")

      def test_80_to_90(self):
                s1 = Student('Bart', 80)
                s2 = Student('Lisa', 87)
                self.assertEqual(s1.getGrade(), 'B')
                self.assertEqual(s2.getGrade(), 'B')
                str = "哈哈哈哈"
                # print("哈哈哈哈")
                print(type(u"str"))


      def test_invalid(self):#测试无效输入
                s1 = Student('Bart',-10)
                s2 = Student('Lisa',-90)
                with self.assertRaises(ValueError) :
                    print("error")
                    value = s1.getGrade()
                with self.assertRaises(ValueError):
                    value = s2.getGrade()
                    print("erroe") #AssertionError: ValueError not raised  如果打印出这句话，表示没有抛出异常

# if __name__ == '__main__':#方便的将一个单元测试模块变为可直接运行的测试脚本，main()方法使用TestLoader类来搜索所有包含在该模块中以“test”命名开头的测试方法，并自动执行他们
#                 unittest.main()
suite = unittest.TestLoader().loadTestsFromTestCase(testStudent)
unittest.TextTestRunner(verbosity=2).run(suite)

