#_*_ coding:utf-8 _*_
#_author: "Administrator"
#date: 2017/11/7
'''
创建北京，上海两所学校
创建linux，python，go，三个课程，；linux/pythong 在北京开,go,在上海开
课程包括周期，价格，通过学校创建课程
通过学校创建班级，班级关联课程，讲师
创建学员时，选择学校，关联班级
创建讲师角色时关联学校
提供两个角色接口
学员视图，可以注册，交学费，选择班级
讲师视图，可以管理自己的班级，上课时选择班级，查看班级学院列表，修改所管理的学院的成绩
管理视图，创建讲师，创建班级，创建课程
'''
import sys,json


