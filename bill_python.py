#full program to find the total bill of the menu items with gst
food_dict={
    'idli':10,
    'dosa':20,
    'vada' : 5,
    'pongal':30,
    'poori':25
}

#food_dict
food_order = list(input().split())   #getting input from user

def con_fun(a):
    ite = iter(a)
    ord_dic = dict(zip(ite,ite))
    return ord_dic

ord_dic = con_fun(food_order)

def cal_price(ord_item,menu_item):
    res = []
    for ke,val in ord_item.items():
        if ke in menu_item.keys():
            #print(ke,val,ord_item.items())
            res1 = (float(ord_item[ke])*menu_item[ke])+(float(ord_item[ke])*menu_item[ke])*(5/100)
            res.append(round(res1,2))
        else:
            return ke +' not in menu'
    return (sum(res))
        
res= cal_price(ord_dic,food_dict)
res
                