import dal.functions as dal


def answer_rfq(incoming_rfq):
    price_stock_hist = dal.get_prices(incoming_rfq.get_sym())
    price_stock_hist_ret = price_stock_hist.pct_change() * incoming_rfq.get_qty() / abs(incoming_rfq.get_qty())

    z_dict = {
        0.8: 1.0050000001,
        1: 1.000000001,
        -0.8: 0.99499999999,
        -1: 0.989999999999
    }

    rtn_z = ((price_stock_hist_ret.iloc[-1] - price_stock_hist_ret.iloc[-10:].mean()) / price_stock_hist_ret.iloc[
                                                                                        -60:].std()).values

    rtn_multiplier = z_dict[min(z_dict.keys(), key=lambda x: abs(x - rtn_z))]

    return price_stock_hist.iloc[-1].values[0] * rtn_multiplier
