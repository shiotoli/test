# coding: UTF-8

from WindPy import *
import json
import datetime
def datetime2str(date):
    return "%d-%02d-%02d"%(date.year,date.month,date.day)
class stock:
    def stock(self, id):
        self.id = id;
        self.ipo_date = None;

today = datetime.date.today()
yesterday = datetime.date.today()+datetime.timedelta(-1)
date_str = "date="+datetime2str(today)
print date_str
w.start();
# get_today_stock_idw.wset("sectorconstituent","date=2016-08-27;sectorid=a001010100000000;field=wind_code,sec_name")
# AllAStock =w.wset("SectorConstituent","date=%d%02d%02d;sectorId=a001010100000000;field=wind_code,sec_name"%(today.year,today.month,today.day));
# if AllAStock.ErrorCode != 0:
#     print("Get Data failed! exit!")
#     exit()
#
# with open('data\\AllAStock_id.json',mode='w') as f2:json.dump(AllAStock.Data[0],f2);
# with open('data\\AllAStock_name.json',mode='w') as f3:json.dump(AllAStock.Data[1],f3,encoding='utf-8');

data = []
###get all stock
# with open('data\\AllAStock_id.json', 'r') as f:AllAStock = json.load(f)
###get ipo Data
# for stock in AllAStock:
#     print stock
#     re = w.wsd(stock, "ipo_date", datetime2str(yesterday), datetime2str(today), "Period=Q")
#     if re.ErrorCode != 0:
#         print("Get Data failed! exit!")
#         exit()
#     d = dict()
#     d["id"] = stock;
#     d["ipo_date"] = datetime2str(re.Data[0][0])
#     data.append(d)
#     # print data
#     with open('data\\ipo_date.json', mode='w') as f2:
#         json.dump(data, f2);
# # print ','.join(AllAStock)
# print w.wsd("000001.SZ", "ipo_date", "", "", "")
# w.wsd("000001.SZ", "monetary_cap,tradable_fin_assets,notes_rcv,acct_rcv,oth_rcv,prepay,dvd_rcv,int_rcv,inventories,consumptive_bio_assets,deferred_exp,hfs_assets,non_cur_assets_due_within_1y,settle_rsrv,loans_to_oth_banks,margin_acct,prem_rcv,rcv_from_reinsurer,rcv_from_ceded_insur_cont_rsrv,red_monetary_cap_for_sale,tot_acct_rcv,oth_cur_assets,tot_cur_assets,fin_assets_avail_for_sale,held_to_mty_invest,invest_real_estate,long_term_eqy_invest,long_term_rec,fix_assets,proj_matl,const_in_prog,fix_assets_disp,productive_bio_assets,oil_and_natural_gas_assets,intang_assets,r_and_d_costs,goodwill,long_term_deferred_exp,deferred_tax_assets,loans_and_adv_granted,oth_non_cur_assets,tot_non_cur_assets,cash_deposits_central_bank,agency_bus_assets,rcv_invest,asset_dep_oth_banks_fin_inst,precious_metals,rcv_ceded_unearned_prem_rsrv,rcv_ceded_claim_rsrv,rcv_ceded_life_insur_rsrv,rcv_ceded_lt_health_insur_rsrv,insured_pledge_loan,cap_mrgn_paid,independent_acct_assets,time_deposits,subr_rec,mrgn_paid,seat_fees_exchange,clients_cap_deposit,clients_rsrv_settle,oth_assets,derivative_fin_assets,tot_assets,st_borrow,tradable_fin_liab,notes_payable,acct_payable,adv_from_cust,empl_ben_payable,taxes_surcharges_payable,tot_acct_payable,int_payable,dvd_payable,oth_payable,acc_exp,deferred_inc_cur_liab,hfs_liab,non_cur_liab_due_within_1y,st_bonds_payable,borrow_central_bank,deposit_received_ib_deposits,loans_oth_banks,fund_sales_fin_assets_rp,handling_charges_comm_payable,payable_to_reinsurer,rsrv_insur_cont,acting_trading_sec,acting_uw_sec,oth_cur_liab,tot_cur_liab,lt_borrow,bonds_payable,lt_payable,lt_empl_ben_payable,specific_item_payable,provisions,deferred_tax_liab,deferred_inc_non_cur_liab,oth_non_cur_liab,tot_non_cur_liab,liab_dep_oth_banks_fin_inst,agency_bus_liab,cust_bank_dep,claims_payable,dvd_payable_insured,deposit_received,insured_deposit_invest,unearned_prem_rsrv,out_loss_rsrv,life_insur_rsrv,lt_health_insur_v,independent_acct_liab,prem_received_adv,pledge_loan,st_finl_inst_payable,oth_liab,derivative_fin_liab,tot_liab,cap_stk,other_equity_instruments,other_equity_instruments_PRE,cap_rsrv,surplus_rsrv,undistributed_profit,tsy_stk,other_compreh_inc_bs,special_rsrv,prov_nom_risks,cnvd_diff_foreign_curr_stat,unconfirmed_invest_loss_bs,minority_int,eqy_belongto_parcomsh,tot_equity,tot_liab_shrhldr_eqy,qfa_tot_oper_rev,qfa_oper_rev,qfa_interest_inc,qfa_insur_prem_unearned,qfa_handling_chrg_comm_inc,qfa_tot_prem_inc,qfa_reinsur_inc,qfa_prem_ceded,qfa_unearned_prem_rsrv,qfa_net_inc_agency business,qfa_net_inc_underwriting-business,qfa_net_inc_customerasset-management business,qfa_other_oper_inc,qfa_net_int_inc,qfa_net_fee_and_commission_inc,qfa_net_other_oper_inc,qfa_tot_oper_cost,qfa_oper_cost,qfa_grossmargin,qfa_interest_exp,qfa_handling_chrg_comm_exp,qfa_oper_exp,qfa_taxes_surcharges_ops,qfa_selling_dist_exp,qfa_gerl_admin_exp,qfa_fin_exp_is,qfa_impair_loss_assets,qfa_prepay_surr,qfa_net_claim_exp,qfa_net_insur_cont_rsrv,qfa_dvd_exp_insured,qfa_reinsurance_exp,qfa_claim_exp_recoverable,qfa_Insur_rsrv_recoverable,qfa_reinsur_exp_recoverable,qfa_other_oper_exp,qfa_net_gain_chg_fv,qfa_net_invest_inc,qfa_inc_invest_assoc_jv_entp,qfa_net_gain_fx_trans,qfa_opprofit,qfa_non_oper_rev,qfa_non_oper_exp,qfa_net_loss_disp_noncur_asset,qfa_tot_profit,qfa_tax,qfa_unconfirmed_invest_loss_is,qfa_net_profit_is,qfa_minority_int_inc,qfa_np_belongto_parcomsh,qfa_other_compreh_inc,qfa_tot_compreh_inc,qfa_tot_compreh_inc_min_shrhldr,qfa_tot_compreh_inc_parent_comp,qfa_cash_recp_sg_and_rs,qfa_recp_tax_rends,qfa_other_cash_recp_ral_oper_act,qfa_net_incr_insured_dep,qfa_net_incr_dep_cob,qfa_net_incr_loans_central_bank,qfa_net_incr_fund_borr_ofi,qfa_net_incr_int_handling_chrg,qfa_cash_recp_prem_orig_inco,qfa_net_cash_received_reinsu_bus,qfa_net_incr_disp_tfa,qfa_net_incr_disp_fin_assets_avail,qfa_net_incr_loans_other_bank,qfa_net_incr_repurch_bus_fund,qfa_stot_cash_inflows_oper_act,qfa_cash_pay_goods_purch_serv_rec,qfa_cash_pay_beh_empl,qfa_pay_all_typ_tax,qfa_other_cash_pay_ral_oper_act,qfa_net_incr_clients_loan_adv,qfa_net_incr_dep_cbob,qfa_cash_pay_claims_orig_inco,qfa_handling_chrg_paid,qfa_comm_insur_plcy_paid,qfa_stot_cash_outflows_oper_act,qfa_net_cash_flows_oper_act,qfa_cash_recp_disp_withdrwl_invest,qfa_cash_recp_return_invest,qfa_net_cash_recp_disp_fiolta,qfa_net_cash_recp_disp_sobu,qfa_other_cash_recp_ral_inv_act,qfa_stot_cash_inflows_inv_act,qfa_cash_pay_acq_const_fiolta,qfa_cash_paid_invest,qfa_net_incr_pledge_loan,qfa_net_cash_pay_aquis_sobu,qfa_other_cash_pay_ral_inv_act,qfa_stot_cash_outflows_inv_act,qfa_net_cash_flows_inv_act,qfa_cash_recp_cap_contrib,qfa_cash_rec_saims,qfa_cash_recp_borrow,qfa_other_cash_recp_ral_fnc_act,qfa_proc_issue_bonds,qfa_stot_cash_inflows_fnc_act,qfa_cash_prepay_amt_borr,qfa_cash_pay_dist_dpcp_int_exp,qfa_dvd_profit_paid_sc_ms,qfa_other_cash_pay_ral_fnc_act,qfa_stot_cash_outflows_fnc_act,qfa_net_cash_flows_fnc_act,qfa_eff_fx_flu_cash,qfa_net_incr_cash_cash_equ_dm,qfa_cash_cash_equ_end_period,qfa_net_profit_cs,qfa_prov_depr_assets,qfa_depr_fa_coga_dpba,qfa_amort_intang_assets,qfa_amort_lt_deferred_exp,qfa_decr_deferred_exp,qfa_incr_acc_exp,qfa_loss_disp_fiolta,qfa_loss_scr_fa,qfa_loss_fv_chg,qfa_fin_exp_cs,qfa_invest_loss,qfa_deferred_tax_assets_decr,qfa_incr_deferred_inc_tax_liab,qfa_decr_inventories,qfa_decr_oper_payable,qfa_incr_oper_payable,qfa_unconfirmed_invest_loss_cs,qfa_others,qfa_im_net_cash_flows_oper_act,qfa_conv_debt_into_cap,qfa_conv_corp_bonds_due_within_1y,qfa_fa_fnc_leases,qfa_end_bal_cash,qfa_end_bal_cash_equ,qfa_net_incr_cash_cash_equ_im", "2016-08-15", "2016-09-13", "rptType=1;Period=Q")
all_param_name_non_split = "monetary_cap,tradable_fin_assets,notes_rcv,acct_rcv,oth_rcv,prepay,dvd_rcv,int_rcv,inventories,consumptive_bio_assets,deferred_exp,hfs_assets,non_cur_assets_due_within_1y,settle_rsrv,loans_to_oth_banks,margin_acct,prem_rcv,rcv_from_reinsurer,rcv_from_ceded_insur_cont_rsrv,red_monetary_cap_for_sale,tot_acct_rcv,oth_cur_assets,tot_cur_assets,fin_assets_avail_for_sale,held_to_mty_invest,invest_real_estate,long_term_eqy_invest,long_term_rec,fix_assets,proj_matl,const_in_prog,fix_assets_disp,productive_bio_assets,oil_and_natural_gas_assets,intang_assets,r_and_d_costs,goodwill,long_term_deferred_exp,deferred_tax_assets,loans_and_adv_granted,oth_non_cur_assets,tot_non_cur_assets,cash_deposits_central_bank,agency_bus_assets,rcv_invest,asset_dep_oth_banks_fin_inst,precious_metals,rcv_ceded_unearned_prem_rsrv,rcv_ceded_claim_rsrv,rcv_ceded_life_insur_rsrv,rcv_ceded_lt_health_insur_rsrv,insured_pledge_loan,cap_mrgn_paid,independent_acct_assets,time_deposits,subr_rec,mrgn_paid,seat_fees_exchange,clients_cap_deposit,clients_rsrv_settle,oth_assets,derivative_fin_assets,tot_assets,st_borrow,tradable_fin_liab,notes_payable,acct_payable,adv_from_cust,empl_ben_payable,taxes_surcharges_payable,tot_acct_payable,int_payable,dvd_payable,oth_payable,acc_exp,deferred_inc_cur_liab,hfs_liab,non_cur_liab_due_within_1y,st_bonds_payable,borrow_central_bank,deposit_received_ib_deposits,loans_oth_banks,fund_sales_fin_assets_rp,handling_charges_comm_payable,payable_to_reinsurer,rsrv_insur_cont,acting_trading_sec,acting_uw_sec,oth_cur_liab,tot_cur_liab,lt_borrow,bonds_payable,lt_payable,lt_empl_ben_payable,specific_item_payable,provisions,deferred_tax_liab,deferred_inc_non_cur_liab,oth_non_cur_liab,tot_non_cur_liab,liab_dep_oth_banks_fin_inst,agency_bus_liab,cust_bank_dep,claims_payable,dvd_payable_insured,deposit_received,insured_deposit_invest,unearned_prem_rsrv,out_loss_rsrv,life_insur_rsrv,lt_health_insur_v,independent_acct_liab,prem_received_adv,pledge_loan,st_finl_inst_payable,oth_liab,derivative_fin_liab,tot_liab,cap_stk,other_equity_instruments,other_equity_instruments_PRE,cap_rsrv,surplus_rsrv,undistributed_profit,tsy_stk,other_compreh_inc_bs,special_rsrv,prov_nom_risks,cnvd_diff_foreign_curr_stat,unconfirmed_invest_loss_bs,minority_int,eqy_belongto_parcomsh,tot_equity,tot_liab_shrhldr_eqy,qfa_tot_oper_rev,qfa_oper_rev,qfa_interest_inc,qfa_insur_prem_unearned,qfa_handling_chrg_comm_inc,qfa_tot_prem_inc,qfa_reinsur_inc,qfa_prem_ceded,qfa_unearned_prem_rsrv,qfa_net_inc_agency business,qfa_net_inc_underwriting-business,qfa_net_inc_customerasset-management business,qfa_other_oper_inc,qfa_net_int_inc,qfa_net_fee_and_commission_inc,qfa_net_other_oper_inc,qfa_tot_oper_cost,qfa_oper_cost,qfa_grossmargin,qfa_interest_exp,qfa_handling_chrg_comm_exp,qfa_oper_exp,qfa_taxes_surcharges_ops,qfa_selling_dist_exp,qfa_gerl_admin_exp,qfa_fin_exp_is,qfa_impair_loss_assets,qfa_prepay_surr,qfa_net_claim_exp,qfa_net_insur_cont_rsrv,qfa_dvd_exp_insured,qfa_reinsurance_exp,qfa_claim_exp_recoverable,qfa_Insur_rsrv_recoverable,qfa_reinsur_exp_recoverable,qfa_other_oper_exp,qfa_net_gain_chg_fv,qfa_net_invest_inc,qfa_inc_invest_assoc_jv_entp,qfa_net_gain_fx_trans,qfa_opprofit,qfa_non_oper_rev,qfa_non_oper_exp,qfa_net_loss_disp_noncur_asset,qfa_tot_profit,qfa_tax,qfa_unconfirmed_invest_loss_is,qfa_net_profit_is,qfa_minority_int_inc,qfa_np_belongto_parcomsh,qfa_other_compreh_inc,qfa_tot_compreh_inc,qfa_tot_compreh_inc_min_shrhldr,qfa_tot_compreh_inc_parent_comp,qfa_cash_recp_sg_and_rs,qfa_recp_tax_rends,qfa_other_cash_recp_ral_oper_act,qfa_net_incr_insured_dep,qfa_net_incr_dep_cob,qfa_net_incr_loans_central_bank,qfa_net_incr_fund_borr_ofi,qfa_net_incr_int_handling_chrg,qfa_cash_recp_prem_orig_inco,qfa_net_cash_received_reinsu_bus,qfa_net_incr_disp_tfa,qfa_net_incr_disp_fin_assets_avail,qfa_net_incr_loans_other_bank,qfa_net_incr_repurch_bus_fund,qfa_stot_cash_inflows_oper_act,qfa_cash_pay_goods_purch_serv_rec,qfa_cash_pay_beh_empl,qfa_pay_all_typ_tax,qfa_other_cash_pay_ral_oper_act,qfa_net_incr_clients_loan_adv,qfa_net_incr_dep_cbob,qfa_cash_pay_claims_orig_inco,qfa_handling_chrg_paid,qfa_comm_insur_plcy_paid,qfa_stot_cash_outflows_oper_act,qfa_net_cash_flows_oper_act,qfa_cash_recp_disp_withdrwl_invest,qfa_cash_recp_return_invest,qfa_net_cash_recp_disp_fiolta,qfa_net_cash_recp_disp_sobu,qfa_other_cash_recp_ral_inv_act,qfa_stot_cash_inflows_inv_act,qfa_cash_pay_acq_const_fiolta,qfa_cash_paid_invest,qfa_net_incr_pledge_loan,qfa_net_cash_pay_aquis_sobu,qfa_other_cash_pay_ral_inv_act,qfa_stot_cash_outflows_inv_act,qfa_net_cash_flows_inv_act,qfa_cash_recp_cap_contrib,qfa_cash_rec_saims,qfa_cash_recp_borrow,qfa_other_cash_recp_ral_fnc_act,qfa_proc_issue_bonds,qfa_stot_cash_inflows_fnc_act,qfa_cash_prepay_amt_borr,qfa_cash_pay_dist_dpcp_int_exp,qfa_dvd_profit_paid_sc_ms,qfa_other_cash_pay_ral_fnc_act,qfa_stot_cash_outflows_fnc_act,qfa_net_cash_flows_fnc_act,qfa_eff_fx_flu_cash,qfa_net_incr_cash_cash_equ_dm,qfa_cash_cash_equ_end_period,qfa_net_profit_cs,qfa_prov_depr_assets,qfa_depr_fa_coga_dpba,qfa_amort_intang_assets,qfa_amort_lt_deferred_exp,qfa_decr_deferred_exp,qfa_incr_acc_exp,qfa_loss_disp_fiolta,qfa_loss_scr_fa,qfa_loss_fv_chg,qfa_fin_exp_cs,qfa_invest_loss,qfa_deferred_tax_assets_decr,qfa_incr_deferred_inc_tax_liab,qfa_decr_inventories,qfa_decr_oper_payable,qfa_incr_oper_payable,qfa_unconfirmed_invest_loss_cs,qfa_others,qfa_im_net_cash_flows_oper_act,qfa_conv_debt_into_cap,qfa_conv_corp_bonds_due_within_1y,qfa_fa_fnc_leases,qfa_end_bal_cash,qfa_end_bal_cash_equ,qfa_net_incr_cash_cash_equ_im"
all_param_name =  all_param_name_non_split.split(',')
# all_param_name=["monetary_cap,tradable_fin_assets,notes_rcv,acct_rcv,oth_rcv,prepay,dvd_rcv,int_rcv,inventories,consumptive_bio_assets,deferred_exp,hfs_assets,non_cur_assets_due_within_1y,settle_rsrv,loans_to_oth_banks,margin_acct,prem_rcv,rcv_from_reinsurer,rcv_from_ceded_insur_cont_rsrv,red_monetary_cap_for_sale,tot_acct_rcv,oth_cur_assets,tot_cur_assets,fin_assets_avail_for_sale,held_to_mty_invest,invest_real_estate,long_term_eqy_invest,long_term_rec,fix_assets,proj_matl,const_in_prog,fix_assets_disp,productive_bio_assets,oil_and_natural_gas_assets,intang_assets,r_and_d_costs,goodwill,long_term_deferred_exp,deferred_tax_assets,loans_and_adv_granted,oth_non_cur_assets,tot_non_cur_assets,cash_deposits_central_bank,agency_bus_assets,rcv_invest,asset_dep_oth_banks_fin_inst,precious_metals,rcv_ceded_unearned_prem_rsrv,rcv_ceded_claim_rsrv,rcv_ceded_life_insur_rsrv,rcv_ceded_lt_health_insur_rsrv,insured_pledge_loan,cap_mrgn_paid,independent_acct_assets,time_deposits,subr_rec,mrgn_paid,seat_fees_exchange,clients_cap_deposit,clients_rsrv_settle,oth_assets,derivative_fin_assets,tot_assets,st_borrow,tradable_fin_liab,notes_payable,acct_payable,adv_from_cust,empl_ben_payable,taxes_surcharges_payable,tot_acct_payable,int_payable,dvd_payable,oth_payable,acc_exp,deferred_inc_cur_liab,hfs_liab,non_cur_liab_due_within_1y,st_bonds_payable,borrow_central_bank,deposit_received_ib_deposits,loans_oth_banks,fund_sales_fin_assets_rp,handling_charges_comm_payable,payable_to_reinsurer,rsrv_insur_cont,acting_trading_sec,acting_uw_sec,oth_cur_liab,tot_cur_liab,lt_borrow,bonds_payable,lt_payable,lt_empl_ben_payable,specific_item_payable,provisions,deferred_tax_liab,deferred_inc_non_cur_liab,oth_non_cur_liab,tot_non_cur_liab,liab_dep_oth_banks_fin_inst,agency_bus_liab,cust_bank_dep,claims_payable,dvd_payable_insured,deposit_received,insured_deposit_invest,unearned_prem_rsrv,out_loss_rsrv,life_insur_rsrv,lt_health_insur_v,independent_acct_liab,prem_received_adv,pledge_loan,st_finl_inst_payable,oth_liab,derivative_fin_liab,tot_liab,cap_stk,other_equity_instruments,other_equity_instruments_PRE,cap_rsrv,surplus_rsrv,undistributed_profit,tsy_stk,other_compreh_inc_bs,special_rsrv,prov_nom_risks,cnvd_diff_foreign_curr_stat,unconfirmed_invest_loss_bs,minority_int,eqy_belongto_parcomsh,tot_equity,tot_liab_shrhldr_eqy,qfa_tot_oper_rev,qfa_oper_rev,qfa_interest_inc,qfa_insur_prem_unearned,qfa_handling_chrg_comm_inc,qfa_tot_prem_inc,qfa_reinsur_inc,qfa_prem_ceded,qfa_unearned_prem_rsrv,qfa_net_inc_agency business,qfa_net_inc_underwriting-business,qfa_net_inc_customerasset-management business,qfa_other_oper_inc,qfa_net_int_inc,qfa_net_fee_and_commission_inc,qfa_net_other_oper_inc,qfa_tot_oper_cost,qfa_oper_cost,qfa_grossmargin,qfa_interest_exp,qfa_handling_chrg_comm_exp,qfa_oper_exp,qfa_taxes_surcharges_ops,qfa_selling_dist_exp,qfa_gerl_admin_exp,qfa_fin_exp_is,qfa_impair_loss_assets,qfa_prepay_surr,qfa_net_claim_exp,qfa_net_insur_cont_rsrv,qfa_dvd_exp_insured,qfa_reinsurance_exp,qfa_claim_exp_recoverable,qfa_Insur_rsrv_recoverable,qfa_reinsur_exp_recoverable,qfa_other_oper_exp,qfa_net_gain_chg_fv,qfa_net_invest_inc,qfa_inc_invest_assoc_jv_entp,qfa_net_gain_fx_trans,qfa_opprofit,qfa_non_oper_rev,qfa_non_oper_exp,qfa_net_loss_disp_noncur_asset,qfa_tot_profit,qfa_tax,qfa_unconfirmed_invest_loss_is,qfa_net_profit_is,qfa_minority_int_inc,qfa_np_belongto_parcomsh,qfa_other_compreh_inc,qfa_tot_compreh_inc,qfa_tot_compreh_inc_min_shrhldr,qfa_tot_compreh_inc_parent_comp,qfa_cash_recp_sg_and_rs,qfa_recp_tax_rends,qfa_other_cash_recp_ral_oper_act,qfa_net_incr_insured_dep,qfa_net_incr_dep_cob,qfa_net_incr_loans_central_bank,qfa_net_incr_fund_borr_ofi,qfa_net_incr_int_handling_chrg,qfa_cash_recp_prem_orig_inco,qfa_net_cash_received_reinsu_bus,qfa_net_incr_disp_tfa,qfa_net_incr_disp_fin_assets_avail,qfa_net_incr_loans_other_bank,qfa_net_incr_repurch_bus_fund,qfa_stot_cash_inflows_oper_act,qfa_cash_pay_goods_purch_serv_rec,qfa_cash_pay_beh_empl,qfa_pay_all_typ_tax,qfa_other_cash_pay_ral_oper_act,qfa_net_incr_clients_loan_adv,qfa_net_incr_dep_cbob,qfa_cash_pay_claims_orig_inco,qfa_handling_chrg_paid,qfa_comm_insur_plcy_paid,qfa_stot_cash_outflows_oper_act,qfa_net_cash_flows_oper_act,qfa_cash_recp_disp_withdrwl_invest,qfa_cash_recp_return_invest,qfa_net_cash_recp_disp_fiolta,qfa_net_cash_recp_disp_sobu,qfa_other_cash_recp_ral_inv_act,qfa_stot_cash_inflows_inv_act,qfa_cash_pay_acq_const_fiolta,qfa_cash_paid_invest,qfa_net_incr_pledge_loan,qfa_net_cash_pay_aquis_sobu,qfa_other_cash_pay_ral_inv_act,qfa_stot_cash_outflows_inv_act,qfa_net_cash_flows_inv_act,qfa_cash_recp_cap_contrib,qfa_cash_rec_saims,qfa_cash_recp_borrow,qfa_other_cash_recp_ral_fnc_act,qfa_proc_issue_bonds,qfa_stot_cash_inflows_fnc_act,qfa_cash_prepay_amt_borr,qfa_cash_pay_dist_dpcp_int_exp,qfa_dvd_profit_paid_sc_ms,qfa_other_cash_pay_ral_fnc_act,qfa_stot_cash_outflows_fnc_act,qfa_net_cash_flows_fnc_act,qfa_eff_fx_flu_cash,qfa_net_incr_cash_cash_equ_dm,qfa_cash_cash_equ_end_period,qfa_net_profit_cs,qfa_prov_depr_assets,qfa_depr_fa_coga_dpba,qfa_amort_intang_assets,qfa_amort_lt_deferred_exp,qfa_decr_deferred_exp,qfa_incr_acc_exp,qfa_loss_disp_fiolta,qfa_loss_scr_fa,qfa_loss_fv_chg,qfa_fin_exp_cs,qfa_invest_loss,qfa_deferred_tax_assets_decr,qfa_incr_deferred_inc_tax_liab,qfa_decr_inventories,qfa_decr_oper_payable,qfa_incr_oper_payable,qfa_unconfirmed_invest_loss_cs,qfa_others,qfa_im_net_cash_flows_oper_act,qfa_conv_debt_into_cap,qfa_conv_corp_bonds_due_within_1y,qfa_fa_fnc_leases,qfa_end_bal_cash,qfa_end_bal_cash_equ,qfa_net_incr_cash_cash_equ_im"]

# re = w.wsd("000001.SZ", "monetary_cap,tradable_fin_assets,notes_rcv,acct_rcv,oth_rcv,prepay,dvd_rcv,int_rcv,inventories,consumptive_bio_assets,deferred_exp,hfs_assets,non_cur_assets_due_within_1y,settle_rsrv,loans_to_oth_banks,margin_acct,prem_rcv,rcv_from_reinsurer,rcv_from_ceded_insur_cont_rsrv,red_monetary_cap_for_sale,tot_acct_rcv,oth_cur_assets,tot_cur_assets,fin_assets_avail_for_sale,held_to_mty_invest,invest_real_estate,long_term_eqy_invest,long_term_rec,fix_assets,proj_matl,const_in_prog,fix_assets_disp,productive_bio_assets,oil_and_natural_gas_assets,intang_assets,r_and_d_costs,goodwill,long_term_deferred_exp,deferred_tax_assets,loans_and_adv_granted,oth_non_cur_assets,tot_non_cur_assets,cash_deposits_central_bank,agency_bus_assets,rcv_invest,asset_dep_oth_banks_fin_inst,precious_metals,rcv_ceded_unearned_prem_rsrv,rcv_ceded_claim_rsrv,rcv_ceded_life_insur_rsrv,rcv_ceded_lt_health_insur_rsrv,insured_pledge_loan,cap_mrgn_paid,independent_acct_assets,time_deposits,subr_rec,mrgn_paid,seat_fees_exchange,clients_cap_deposit,clients_rsrv_settle,oth_assets,derivative_fin_assets,tot_assets,st_borrow,tradable_fin_liab,notes_payable,acct_payable,adv_from_cust,empl_ben_payable,taxes_surcharges_payable,tot_acct_payable,int_payable,dvd_payable,oth_payable,acc_exp,deferred_inc_cur_liab,hfs_liab,non_cur_liab_due_within_1y,st_bonds_payable,borrow_central_bank,deposit_received_ib_deposits,loans_oth_banks,fund_sales_fin_assets_rp,handling_charges_comm_payable,payable_to_reinsurer,rsrv_insur_cont,acting_trading_sec,acting_uw_sec,oth_cur_liab,tot_cur_liab,lt_borrow,bonds_payable,lt_payable,lt_empl_ben_payable,specific_item_payable,provisions,deferred_tax_liab,deferred_inc_non_cur_liab,oth_non_cur_liab,tot_non_cur_liab,liab_dep_oth_banks_fin_inst,agency_bus_liab,cust_bank_dep,claims_payable,dvd_payable_insured,deposit_received,insured_deposit_invest,unearned_prem_rsrv,out_loss_rsrv,life_insur_rsrv,lt_health_insur_v,independent_acct_liab,prem_received_adv,pledge_loan,st_finl_inst_payable,oth_liab,derivative_fin_liab,tot_liab,cap_stk,other_equity_instruments,other_equity_instruments_PRE,cap_rsrv,surplus_rsrv,undistributed_profit,tsy_stk,other_compreh_inc_bs,special_rsrv,prov_nom_risks,cnvd_diff_foreign_curr_stat,unconfirmed_invest_loss_bs,minority_int,eqy_belongto_parcomsh,tot_equity,tot_liab_shrhldr_eqy,qfa_tot_oper_rev,qfa_oper_rev,qfa_interest_inc,qfa_insur_prem_unearned,qfa_handling_chrg_comm_inc,qfa_tot_prem_inc,qfa_reinsur_inc,qfa_prem_ceded,qfa_unearned_prem_rsrv,qfa_net_inc_agency business,qfa_net_inc_underwriting-business,qfa_net_inc_customerasset-management business", "2013-06-13", "2016-09-13", "rptType=1;Period=Q")
data = []
with open('data\\ipo_date.json','r') as f:Allstock = json.load(f)
import os
filter_id = os.listdir('data\\')
for stock in Allstock:
    if stock["id"]+".json" in filter_id:
        continue
    print stock["id"]
    start_date = "2006-01-01"
    if stock["ipo_date"]>start_date:
        # print stock["ipo_date"]
        start_date = stock["ipo_date"]
    # continue
    re = w.wsd(stock["id"],all_param_name_non_split,start_date, options="rptType=1;Period=Q")
    if re.ErrorCode != 0:
        print "error_code = "+str(re.ErrorCode)
        print("Get Data failed! exit!")
        exit()
    tmp = dict()
    tmp["id"] = stock["id"]
    tmp["ipo_date"] = stock["ipo_date"]
    report = []
    for i in range(len(re.Times)-1):
        temp = dict()
        print re.Times[i]
        temp["times"] = datetime2str(re.Times[i])
        # print len(re.Data)
        # print len(re.Times)
        # print len(re.Data[i])
        # print len(all_param_name)
        for j in range(len(all_param_name)):
            temp[all_param_name[j]]=re.Data[j][i]
        report.append(temp)
    tmp["report"] = report
    data.append(tmp)
    with open('data\\%s.json' % tmp["id"], mode='w') as f2:
        json.dump(tmp, f2,indent=2);
# print re