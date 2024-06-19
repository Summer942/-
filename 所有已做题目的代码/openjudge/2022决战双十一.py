n,m=map(int,input().split())
goods={}
coupons={}
for i in range(n):
    goods_i={}
    shops_prices=input().split()
    for shop_price in shops_prices:
        shop,price=map(int,shop_price.split(':'))
        goods_i[shop]=price
    goods[i+1]=goods_i #第i个商品对应一个字典
for ii in range(m):
    coupons_ii=[]
    as_bs=input().split()
    for a_b in as_bs:
        coupons_ii.append(list(map(int,a_b.split('-'))))
    coupons[ii+1]=coupons_ii #第ii个店铺对应一个列表
def all_plans(n,goods,num,plan,plans): #num表示当前购买第几个商品
    if num==n+1:
        plans.append(plan[:]) 
#这里用切片创建一个plan的副本而不能用append(plan),否则由于递归调用不会影响上一层的plan，最终添加的依旧是最开始的[]
        return
    for j in goods[num].keys():
        plan.append(j)
        all_plans(n,goods,num+1,plan,plans)
        plan.pop()
    return
def buy(n,m,goods,coupons):                    
    plans=[]
    all_plans(n,goods,1,[],plans)
    res=[]
    for plan in plans:
        separate_cost=[0]*m #各个店铺的消费额
        for k in range(1,n+1):
            for kk in range(m):
                if plan[k-1]==kk+1:
                    separate_cost[kk]+=goods[k][plan[k-1]]
        total_cost=sum(separate_cost)
        total_cost_=total_cost-total_cost//300*50 #跨店满减
        for l in range(m): 
            discount=0 #优惠券
            for ll in range(len(coupons[l+1])):
                if separate_cost[l]>=coupons[l+1][ll][0] and coupons[l+1][ll][1]>=discount: #保证能优惠且优惠力度最大
                    discount=coupons[l+1][ll][1]
            total_cost_-=discount
        res.append(total_cost_)
    return min(res)
print(buy(n,m,goods,coupons))