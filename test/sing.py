def initialize(context):
    enable_profile()

    run_daily(period,time='every_bar')
    set_benchmark('399978.XSHE')
    # 设定好要交易的股票数量
    g.stocksnum = 20
    # 设定交易周期
    g.period = 13
    # 记录策略进行天数
    g.days = 0

def period(context):
    # 判断策略进行天数是否能被轮动频率整除余1
    if g.days % g.period == 0:
        # 代码：找出市值排名最小的前stocksnum只股票作为要买入的股票
        # 获取上证指数和深证综指的成分股代码并连接，即为全A股市场所有股票的股票代码
        # 用加号可以连接两个list
        scu = get_index_stocks('399978.XSHE')
        # 选出在scu内的市值排名最小的前stocksnum只股票
        q=query(valuation.code).filter( valuation.code.in_(scu) ).order_by(valuation.market_cap.asc()).limit(g.stocksnum)
        df = get_fundamentals(q)
        # 选取股票代码并转为list
        buylist=list(df['code'])

        # 代码：若已持有的股票的市值已经不够小而不在要买入的股票中，则卖出这些股票。
        # 对于每个当下持有的股票进行判断：现在是否已经不在buylist里，如果是则卖出
        for stock in context.portfolio.positions:
            if stock not in buylist: #如果stock不在buylist
                order_target(stock, 0) #调整stock的持仓为0，即卖出

        # 代码：买入要买入的股票，买入金额为可用资金的stocksnum分之一
        # 将资金分成g.stocksnum份
        position_per_stk = context.portfolio.cash/g.stocksnum
        # 用position_per_stk大小的g.stocksnum份资金去买buylist中的股票
        for stock in buylist:
            order_value(stock, position_per_stk)
    # 策略进行天数增加1
    g.days = g.days + 1