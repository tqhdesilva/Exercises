import string

ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + '-_'
ALPHABET_REVERSE = dict((c,i) for (i,c) in enumerate(ALPHABET))
BASE = len(ALPHABET)

def num_decode(s):
	n = 0
	sLength = len(s)
	for c in s:
		n = n * BASE + ALPHABET_REVERSE[c]
	return n

def NumberPacking(x):
    compressed = 'UTbGF9mfwGROsPHFNm12OEvVASPLe3pP1qc2Rn_aToqt4luYyqWFUxQktot3mzmQ0fDyziJsmCAOGqDmOsLl6Fq7lDfmxz3KneSgefN_5CJA7vmlGQNiU8mD1AkcecppujecWSxa4D1cEtnMEKjfEAbfS-DsKAO9ziyOOfKjGbb5ccDWsOlchdt3VIc3v399k5GXOPf3xLy02gp2T4HOvw32iIxyWIOX6BBoQw0EiB0NC1K7abKJdgZZajYhzbJkto-HpHpnjeBFuiHCLsWBkcGsfgC6J6Q_fAWZgfBhUsY7Ci7H6W_sSdGxDtWpa2BNYmzgyDxeL6LeX5hxmRWCA-9luLDM_T8ogN5HySowCkhlDt4t8-XZGWNZjN0Z9dwb5Ys_b0JwsE4qpw_RsDmzZ1jAGByWbQP3tqvfZkpp50KdCYYRK6q3ItqQmMeq3Izn-Km6KKa2EpsYjEFmCv4QPUzay73IZanrlHw9ZwsmVlX2EGRGS908RHdLmC2IvQwvLpEGe3wC7dw-PBC0GJVh-cmNKtSEMX2EJpj6LUAXv-X3zX7FFqsb6qaN5Z6KsXrA1Ek13x0qM3NVUE2Y0oo7kB4eiHK6FrP9V_T6q9fRzLNmIkEBXvpeI95EK3oFedB0h68WhBe50hrEtVoZ1XsmWMtPTkyzVATmREEs5RBsOjQ44I6e7SwmPIgYvCqR_OeUi62sZ2NXzQffR25a8lyK-JzVWQzbCtz9lnAZOXm37TKCKDuHeF76xv47gNzjirak2kWF9G3otMMvrJdtYXly1D4PE-7NXoexoTV8SzM8flh4u0-zfOdVQcFeDEcDB98gmovM707d0mHtSd8Z3SSpkVfEiLg3NBJCj-U_9ZPXrN5qO0a0hfHLNxcRp9r-3FJWyc5NrfuYYAc7rl5QuOdmMTAk0J1to2veNnmou1BA8_hMu28OjjDHBSb08r-wxTySR5LYmOPdLx1_GWZikUFMAEvAhNETGqH-TqlYu0GV8LGVabBnGYYWdDF59tJu2bCtzGRlL_cLvCJS-Iw6P3t_MvVqet624LhT4hMfROsahaUGX6yK9m_yND66OdAPa2U09xe1AUYJaAuM3CifMKf5kynDS-4PtMXHPSdjHpce-pA727XIXkB_t4EjQQCyPqG4oWqjF3fGsSJL69UDj1f26mxIGvoWwYZSLBmmMciPxCqr6a04nPsdn00XUi6VWjgZMrKwYTSgK4UUIr4PH_gO2yWMGUHNGCDTNbU6UaidfBtwuP-TEsLR9mktIN1uqbK4Y6th06Orhdho2Ieet5pvNGNttZUOyJtmJJoOWwSvo9eYImslTqmN3kt4QYR7RrojnFFtK1B-3xJM8pQZcGCQKoACSF9UpjBCRHaj5EG_YLJlKgPZi7-zi5TtTTpxcEHx3sibUQsMl7sx5FKDnDCKV0qNrii8FReA96lYGD2QGgCF3AqrExQK3mh3lyk_Bmvqp7TlAjJ9k1io9eGX8WmYBcWVapxIyaKv7VmvZZHPQgt5Eyj8Fz0uc6VrvpEMatQaEftgqV9_rps5BbL_9tqzDG6p5bV1kJckqDJ6IyTzRKwhaOdWgzMKZ87ao9OCBhAWRARs93g9LyiGXNfF2r5F5KiK6mFDz39PxtInzjwSACmAxhZN40c0HL8cFmwscC7vr2qbm6ToXl9MTX2nkcfGc8YUSBMFfQameXIwY2xeFNzjKefBgDyqxYbbhiFvfzp2Z1xCwUg-A9iZmYN3N0Id5n8ZfwD1Qo4nuIBvx-LJw_Q4PR9Z9fNDpE0zPh0tq9hN4tSyUuvY-BrW5SVViqBJHbgV1XVhP7sGwBKq8edip2IU3vPKL-AP5OqayIWNp04Qz424jLBi_qZZeG0-nxLC_vdX-NUOzScjfdk__1ePfhO3uuSgwW3-Nuqib5PwBvpx1nRxeq9K3p-W_q9zUOjG9WSGOHDzGfBFpXB4lAxDpYERltM00SJdL6WrI58SCF3DNBE-JQZBXmmCVf7iWhmsyk4bsuL8FVnCE9JoxwO8L9uItyKtyrXYKBi_tIS7GklW2EMxW7mMmuhPiSxgML7o_S59cLY4Mj2g0UTsUp4VUi2ny7lDrp9g0iH9qbyKj4ScQetqLHdWsHO02nQEzJVox6lrv_dE1tMsV12KPFwgx3Gy3UUgmftoJ1unaxZSl5Pc5WxtA11jFVZP-1AY2Thmh4o6tM04ebgz_t-PpKQon-yGk9-h9z8yzygANkvN21sKc48KlH6y3Hby1KhEsyc0eDq-Ve9goH1KTZBmH2hL3d_Up-TpS67vCjrxnq4CQu7CS35KB4dizEI-SoAQupqQP_lD3e_7ZEtvQXTl8eZ3Wmvghw3ugc5jBoBPP1f4Z35W8RpKVHzhmk2sci7N-R9WNlU-0XT1hGLf-uJUiVow94mqFWeAB-Danx33S8uPm1X86y2xUMxCDiIGTssE-JzbR3sfWaJGRCKW7OQVHauoJb94HqvbRYB4CG_ITCV3FK2FCV8L9rdg0WgQCVcYR8mZIiSBDRKldADXUwnbAfqImihu1JTckF00mTvEPQxewruSmkrbDPg3o15WKfo1rK_CMEBPsU7_Vem38ZVwR7xMDLZ3xKEs_uQOdJgV9jT4qGyktLmlGJt80IFZuR8E6s2I9wv7i10pR_cYtxcbRojP-rDKQJjKK7wDRpLijVS5ffSo3YgD2Q9rIvT4sDRo5PNZPU6AMX8Odly8nZQQ3ovKlXHnWfwZ8JYrtq_8dvlTyiW6Bd2krzJdMlmlT535s_Gex-Jvi7yF0tPTFr9k0_mHKwYl45wouv0oASkRtfXuzX_xFLOnMlmc6tFNvf-ijpPGS1JmXMIbGj_BJt2Sk6m8hZDTCKVE5OBEVkjacXACfkoSadL98yw3eH9qNVQRivyW1HhVy2YasXm4bpnjiuGoZqAgSGxma-3yQvgDeKS6hy5y4pKck8AV2zcJi1DfFuCEKZBnWm7IVkF1gaewHG3ncDbLQCUDuYkr9YdE0jjOp3qSqztoooKRw9D7OMEUOITTlGDbbIMGwpFAOu8cFKSu0vbbPPf9sFSno6Oyk1ptpECbwP0r_hhfEByXpjRKR2I887b6r9rESQIVRgWUqWtRihx_vp44JSuO5J7MPZQfUh-KN_k65Ryoiqk4IA0M4qAp0Yccrsc5jReDzaV7V4qzHbYDOjPQPFTk7uXwvcGn6o_i41Z6Ydylhnx7--Cjemoy4tSp-OyxDHYad2ScgU-4jjCmeRcobPF9gAI8tmc47flaE275aVAWhlQEwJRGo6004xPE7xnsSYJh9KSbGZbHuYEemGdRRStrQPeb6X0OKiM5x03Wi3aRf0nREjWqigcMWpR0VLhnrcbJz8oUfD78mvj2RIu-CQ1fquiMDVeUd7MI9Gdf-IudeXWpl0Jx4jbDW2OXTF_aq857OaqnMb2LLiLTWoupebcYlddoBeHHAF0DhC1RUHZooS2OfI360jkcISjR12aVX4VYeZk7vqvSUkeXsNY4FsPklT63aXxarh_AEHWjzLx-LtSOx9zRk5pS1bLPCoDIs418Pb5NXqbAcWv7-_3KQ-0gIKiqckXs3ZkS85L6_o6FQYv_EdQOa3MNrzovcoRHJ_onYOuZuid44swr9St3Sz5y1SMtdmA0rH-GvePHqJmd-nmV4eAYZmMz18gQlwoiXFoziBAHKOnHI5oXeENa8bulsk_C2vFKWHaKx6ReIB8DbV4S6jiMduKzvTbPLcDwN7GMudClZX8EF5zXPJQDBKTvxqrCXtJT-KKzanJXhv78IuxbhQT2xL3e5ON2iGRFEpLtb4RCTkbbZuR7C5-U2a8r28TAqKrpupbd5q-AM36OLa2htRdXn6pxvNUvq4O0_rUdBJIBF8y6OgJeY1ISkFZjvSQJH2zKJ3yJRDikIrHY3KG--M9moxrBt5gwdKPE-GQ1eVn6z0EiDX-1zGxri5HExGh2-5b_VwhUxEyccPM5WquhiBILI60W-gj9t_Hb-MYNNEf6j0qAAyi9xfj-M8Ubxlwi8kgoLO3vrCn_qt18PF5OxEql9xjOla5kxpgvIIPV53dfxsefjVlPTqgxgAOgUfBo6X_n06npbeWBFbWBDXQJ9SdYQrmPO4Jo745cUTCr9YZUyGfoOJUsL54chVol-sETz3CgY4IebquwQczvyjUSUK9yOeCeZ-7Vw6aTU5d60Pe6dtzf8L4FZn61eeEEB0FIWopWrIwC3AIUTjBofpz8PUvuFZLXzwgBH9E8bni3UQaa7kexYQPVE4YCYD-ttEmhJCrN4PqkrxABL_flC2DAxQe5kWAAJ7tIyogT4M1P3xtiGjbn9-Bsiw5lfuP8WPZRh59NjgVvvOJbwGO7gNj2yjjA9A_TCiZoy2UiBwZaOV1M49VtQUshglaTsTi9eKIQ4-knhczjx7TrDN1IbJge3VaisC-XQuzavd0jX6_xLBSUjD0DF9lbtacFLT9o4Q65Fi8WBiDdas0kGtgE2DYvQQB-3wWLbjGV8G0NhmcrFG30FFBt687H2AvJuhf8b3g6Nt7VVXYti_TEDAVo_0CGHybeNXjQPqfOukzO0VLGwrRPFaklFGXZ8pzXfJVOW7oUZj59nHXHPilY2fUv5pcnCluYB7CIqdmpsOTccirjhjF51AXAc8k3j1L8tk2MZnbvl3PNGdbfhUKqyWJpYi1-m6TY7xrTu8Lwx2ktQBoxuTm7jXCz0B-7S5cD3URVB5_mIHVrU-9Yzlm3dA8uC40CG0jVompQe-tZlS-IylaBN54177Dpjh6cD7sfawHDcdx977JbVbCyyWyqnGILxxvtaALNqGOCkJ6BuZiw5UtfcHyXAHl-H4_R503heUFmBJHGEVGjO_M2VjqYiXIaejP_Eo5H2Tx1ObpcEm58NVlvBYbICNi2VbgOEJIK8lc4ibi016p0LaKPBkpvoP-tMrbEI-bp5Rs9uKJoS-fu4xtX8fU43Bl_xTFODUbYQJFyR_GVV4uFNq8cyKhgLuEyjJdrdRkzTH5fZDapieHzb2YTUVdRyJtkOLiBx_fldXVAEQgJsKPK0DoY_Wlq0HEdI5sF1FwzK-QT8H_-THOomzM27-MJFYCd7G8Hs4KCuZGToH-7ZV1cEryDHXWVIcoLLJcNIoqK5JxcqIW_pJnHiML1f-GNQGWL1nJB2O89qrQ25VsxdteSOhhpsMRwzgXCd8s4rO5JQkHQ8x5CB-vPgV4KrQCUCoqXdsp620fE2msNhC_1U8LbtDfdr-uKSueq0NSahaCBzrEG4xlZHaXwiKq0GPXLH9Xx1L588Bi9YXrbHzWlHZkt5IdWi9C-DP-wklcr0FdLb4m50440Pa-PTQH2Gmr6irIZYDKVgIc8n8DqbhwW5McHqu94ylhl4moFSm5sTmYzTLlY6vq1bRbjLmFFspa5RG31ahoLzJWw2A41LWHBnNTCS0FnXjO30rOoZme5rvalHsVnEExnT-JA0AwO9S-7RzXFRP6SKo0zDK796HUCMjQzsqntER0Eq2k5GDMwjLyiWKBzBwppBKZAM6eQWqWEgKHWr9h1TA3MrkzHun3yHQ-N8EpQYPdaRusIVlgIEDRjlEDq8UQpGUd34BA1P9fLupUeHlpzrPUyPnv-e0cOChwBz3gc7o-jtesJk2g40s2-DCu0OQDq8X-Zm-n_bgz0HLD6LvqVYXr4lMMgK_O4QOSzLwItEckpPf1hEuFO0kDsjNuBLFzbjr5LRulq2yeToqCdaXkxVvQJzziErcxRMNdL3WMUab_F54ShE5wOnzh8jm3f0pT4KfssgpyHFmkl8Lsqg3bNTA9lYHEKuPKLlf8ohfaPO05OlQiKofk0COxK2kl7Gz9DzEelb-dDbMZK8X4ujrAQkcXSY7u5ua4yFRjDYWuKgtJE9-Xnlv-OYgjgxknQiBsOrBz2Vsxad4fet_vstijpBgMmScWkfxXQ8Us_VeWpC0UkK7TyelA7ZXc80gtkFQQ50KbI0yuSvrG5yL0NO2gkOPeIR1YFIP-cUPWzhtB_D8IoQ_PRUp628RxGadqulPQ0E8LjfKaes0u3teNTTmMS879SuOL6mCOXylhMnaVJ8ODncwY76UdEaMPNcJzESj17WuNX2ANq6onKAj0qE0WbeMfnqn1BhskI6YZHfx6flJjP7otWVFB_h2POzDZo8yXmYWwvQvVsjwMVpeBrNrBO5tJS42B3SLstTFqSa11ehijHy49K1wVrTlXl5NJ6745_G8u-GRGEbXkiKy6O_kBq8z7yCeOTArlKo4AcfXg2JE_727aeQUWfI_v8LysAZepJ_XuXCVQM8HA1vs_e-YAJ69hYxtlsoTK228bK9BtHkkCj0_MIuM-w6GvdLldVP63cBP-VuKvNZDP4HXIeKQlA82Bh-SlldSZRNoL47nfE-MUCxpuq3BTyG8AxV5WImtCH4SZm8noArFzpwEhndBzXK11Oc7mxld4_GzheBhYiLJ1uho6SZCejVI13Sqonj3jRL1rchhoWVodR7jQPr192oHU8vP54hRHeSTpXq3bzYTL_QYqSoBXPRcWKz8E0_FdbF9OAosAW2t5q3w7ZsGn_0_5EyCKQvcjR6jvO3QYgsu-o4k_H4VAXCMnUQp5LNg-TwYpNhKnJ7OO3I7zA352AzI2OKXqwNkANNYHqkQPM8nl3s1CM-4wYrnUYHsvqWoG1VDIlEhKB6eKAq_c-wR5zWp1Ipcea0WR0w3a4iO1GWtHz4s2FEHELdBvEyqKVMrcfFdwJryfgcbqVvwuOfoBWTHMDABDVu0iU61Zz26f21C3kE7FfxdiC3-mNOyI0oJ3lSr6EwNZWtY96uFrHujTmY4rN1YRQRUuYR0wsvB5yizrEV__6DdmOd2ZWZTrnKEcSFDsFPmTU4ONeTheSYsdv8JWkkfm6aVuvFoa6CLlc6Bl775MaTHJaPo3niznGNHbRqoldIiB774FjL3HTBFa97PS1Py0vtnjhQ_sNiJRk06r1MSA9E_XLutC0ya-fRfz3um2KzG0-Y0gds4nENcWEiOpSPEcDDYNLA1pPPgbrJXGNYk_B9u8TmjQ1JybXXGzU6AG24GND4EOaT73CB4WY2ash3F3TTzQvYWECubuTAXAAS6DKOGFWSUQahGNjJer6bK2dS2xTyQnDGRftD46HNaQHHZh5yZV3G8lNol4hqx8YfQX-ab39BQXTt33z2ubM9-moMNo4gTaYYbtqhiyC32Bgp-X4rKiXht8faWzFD2KkVE9Nes8GfwS87ZEEzovY5VJBrMa1HwpJkNKu0TIYjlasP5xSdHq2RWoDy7r3WM7AXEibHPqsbftvCUL_94eOoft7Lf0TO-oGN0IJ-k562l-KRGQ5yTSfcxi2M5e_8hozgowbH-1Lz3LNZvp9rOAXG1ghTksDb07lkaS8VmdpPEND_9zk1OgbY3GU4vJ3aOw3cF56E3ccMUw8zGVkDoLAvNToRpcrUaVsaj46wMF24i2oYLZAxlfgaNHP1_ZZ29Qzn_A2I6IXI9IIIWgvLoIyJtbn7GeRMYLGDEtGTY9VUch9ODFmFeQj0psslF957_z8BsDwBcrSwSxxVIQ1aMON8mT5oNYlb8UqgVP5pdPHxIiPi03HXwL4ljDib4YtKcB7OqEC-BR3sI8AFUeglwFBpi6BtwIUPrOXypbfJHTnIxSiwpng2ZfAcwTtsIDc2ohCgqsgJVCC3wYabX8WIuyCuEljCPUikkEZzZJgYvRRuLgIsibvOMx2q23kmvKm2gjWn0oYIAeGkixmxQUQhivjJLwvlfeAdCLnuNcxgtaQZBJ8nULRRdUaLacrNEFhC-k1tWGDuD1WNhXQJMEEedszIh7OM6uzBPcb-uIPLnQEemVK1q3iQrP1TxTCynGr-vDKSRMf0P4Ls-1wYdVMWvcK5I0567kwuQ_Nc7FXoZTtaKdc9PEIWzZqhzSx7CG51NEJvnYJ36jAeL7sdhW8ts0I1bDgArFhWsaNMUGesiY14-f1RclASEmu_y_OB_FkcVGnZ6i70x2jw13xgn5riESaFhAApReOKPa2zivem3xvuMlT8Kbk4FPk1lkam0qLm8SnKtsNvkwDjVVP26zx-Ym2CwEaJLatzzpRpLl_BKUDpyMbLhTcv_QJ3Q3KBbf94lkcf_To6RJy_OC4p-IV8I9LzDRfgHR-5HC028dGnwrdsTmWvU3yCEYvq-SOheajYh1T3OrqO7yR3f942_gDM6JDTuOfI5nExJOU0dQhrM5Eo71HSFBXVW3MUfE7Bo7npIqpAQyq97Lgr6UQTI-dPJy_ayiiC86zZM3eU725XvVUZxaUlq-GXRUc6lNJHMUiNUz-Phb_HVtVblGoQwsMIV2bfPi4LG-lY5rQYFUimbOXA4E155GkMrhSA3DxWJKC0py-_aB5Mx0ROX1KyHVcWL0etEzC-bKD9DW9imLdnQR3u2PWGYNqLQaIed-D0Dy6WnPDCk6aN_NaL4Tp2GcsBNmr8wxT5xxQSfWdCAa0O6bCEOzey0pxoq0q_QL0JAKdhYzOiL79w2cUlhEmElfIf9EcmrUGlUNIRb-G50QkZkBQPFFZc9B9j-eJtaDAeGCPvUMtniXn3BJehBPBaD6MtIpgwZJG4Zy-Hyk97ZvOAHXv-90p0DL4fGTVeVKLnZ8EWlcWl9scsXSrssO9zAndh_dlOY3owxBvWLdgxhS36RIFE__BySt5UDa0ym7LIHJ85tbpUT5Rb8BvSBmusqmVtPpzzoUYVOdNl9FSzzD-dl_J5Ua2bNQNkpNkLPo6e0AaKTZ6byjh69p3FactiiRIJliPUD5Zd_SE2jNS81c08VUkQnxlAzB2HBBZmmrZlykT4e13hpyz_jQ-mN3ws8DcjF3T_P7TRsINESdsg1g2UBhwjWeVXmvUpBMWwbIugJbLrH-nDrBqm4A75XHk09Aa8fkBYtxBBmAEcRHPaqGB3LoRFAO2qGAQSwR_2Ls88D5MZ0pI4tNdA7TG2xAB9-6vFFe4qfcv7o25SXvsGkWBubnUddZpigyoK1zsA8CFn2BJFql0I6efChVXhEkNec8DsAxHUyQjLppZYlnsYdLu92idRfVYYyRbr3_cOGFAy9J5f-YQBLKvZoA0yYcipqoT-gLmVL76tMrGOh1paS0axP-caHoqGTo4hnTkJ71LlNt-oS0dPNccuLqMPn4JwpFJFInXdBn_bPFHRu2Hi1hfz-DQm4epo4gt0k0n43WtkVYjuVxniLgWYbH-J0HkTTlDJ7Q2RO-vcTPPF0_hHb1IIuurGjAhY4zF3U5IT_789JN3R50ZldjMvpolMlS0v5uR31Jt4j5vrYYWnMFIhoGIVs6Vzzro9Vc72g-E_sQN8y8SIMkBVscHY0XQP5tPeD_MMqZ48kDV8PYdPrwmuKFjvQ76-pyEOgeCPiGFyDU6yut7PELIDL_kOl8x9u2IyP0OzzAF39TbXoY64tk2UdBPJLNS2bvKjJA_CRHtWna0qibKKzkvxtoejfLN5pDijIMdYSR5PehQss7d7TshH59_lLs9H5FnODvdpH5b2AnJ2HFSd23oYeGYX8zOnjBePi8S1-5LVQ3nnJx7_ryoeWdlZ08lINeSlyZLzB09_L8Bg5e7pvBPsf2YnqD4aFI_7bG1-jprSS_O6fG8eTCfZ-dS04pNbhiZxYPjmsP6R_AWlOVVJgobY8sVtommNjqviyIDi8IJmZm6cUBddqG6YRj4M5tBZ3ldCj1NWAPc9SyIr_DMCj-wbP5cogjw_FZs-2Ez5grDEScZzfaNsXr91uYFrHCwdNDySpj09SjfMs_F6951TvLJ8Z-4QH5Mod4rnQ51XX7A0zPZrKzVoLZr2EZXc04--6BN86I2PHbFIIltuKhvw1O9jTd8GNaJ9UzaKojKvsWgJ8NlVAHSYlenFbIksGXh8fbdFFBcPULA5jDO-8QH9SBW1FFKcXepqVwB6Q9P43CdCidSKZOovHlN8wpH5-70kPe1M3GPiZyLL-C4fCsssQAhe4JaCWGRfuAwv5BiRiPpKomUUScdK-RdNon1f9IpxLXY4SN7XHq6g4GcVnVb_DIqhXu0qO5JVLLwCHDjrZ7D-FneVrHRL4xayMeS5kuiDgBmttxMgqDKZpySGueElsPipvCBSayioornLraC_c22haVXdlj9-beh5ioUN4ot13bcrA7HKerNMrq7P8M6YzakMn1PwbMmzKZNiusXK0NvTdQy3d9nXF47NvWoi6G2dWqP4eqAI4Zeep_NUk-e6QkEd2XtE0IDtnvfedxueqZcvSscURLmnL0uhxY5v5J7aMr9KadQpNl_hMWkQFrUDTarxxmYkGQ1AqdhHraW_4f7kCfW5tXQcxVxxOG5ueA6e88PgXb10jVbdDcEo8YdUPJ1UeQuwg3B8x9T3aAy6UT0hd3A-jt9-f6u9RrNnaniqDkH027Q4R6EVAvraO4s8nn1kDCON3xXKghVPn8xgBrCR5WhFmQYLRQ7w8LgaSc0umvzbcxlDX1CYPZsw4vgvNAwxBi59zFJVpFpV-rO4XxJvSpzbnCOFySPsyWyUm6nAm-fmJiDJ6LTDJQxA-pHA5mL-0vpUV7nVo6dNK3mHOq9qgeT5HpDW34L5LXGc8ggzLM4aoS_rf3U-lcZxxjrpHOHM4ZUWnofLTQd0a8jLGeKX8FQBHaszkYP_hWaXInKswJ1XnrvQEWNBpntl1R52T1BgmCEbQsjxuNV9yYYwwIhAUZEaX8-P-HuSgdqso1Mm77u6o3NhRIUp98d8H19oZepwe2-18V1OWfI7JEADIupRqeRXUDCzicj4V0YJseJ9Zb9_imNaCkoM6GCJ5ZWLR3Pjv7IBfh-z_sGtf3Tzrkrkvat8GOZmFBXTAQK0_rsXoFkW_ZJBMpb6ZFoPWqUMCcTomHde8xlHvNO-d_NYmtWfBkB1r4Mf4rbbGoSoF8T8KS0ihj8hmpX4qvmCX8l7DnqA8WybGptHaV9lYwa_5xKzRgNIQ7Rb1MA8X_sQFK5nc1-cPLNrUiFhWgDsunliDtsFwxnCybbC2KB_UIeG0aETmJnd39So0pulHy4y-QLehp6nckaGHed-d66Co44aJk0eH7dv2rnin8JVguNIZeKHHLBtIaOv3FzeQIigvk3pU7nxAVYNvi632BLnuE3lHK3aBMPJ1uIS160aY-yjtbZ4qtD9W5nlFrL-Ya9KfepZckcsdy5PfncbR6ZD2i7omDdBVC7oSrKr1pUc_dSimnK95NPvCc0beVS2n-f1wEz6A2PD0ccigMjzSsO7_brGbZm-qU7klrJ1O6j2J_e3mf_QP4sh2fF85CQs07SiCD-ocOV_-UaSbosGHeFiHPsc3sLt6o5hNeQ18ca_B37umSoLL20tYVQszX-_TbZhoaazuf6-Nt4_bGQXPZLSydydu2IZ832XEFaiTV9DkvAjuV9aVUIValok9Ya71Btk8xxSa5UTiE2BvN4tY-gOfzXmxEqkGSBc8KDfz6F-JYmVxZOWByJmmtMoUmIHFqQSDcL5qDcMUgfJHF0BiO1KZXTY8P0c4pe2QJeNNxgkdxHJKgxgOJJj377wfv2wM7ty9twI28LEYyUbukqmLru7R54mE6yCOSN8Gay953QCzPpPRfVDLzlQMZalbX_tO19yybUQLAAqk3_eSmYv1g0pbmxPvL1KD-dg1QFxj0ILv5nDG2g2yHfOuotLpMAysivWQ6Z4T60NLuzI5g6E6vIKxuOF2XZn1a_VBuLZ9KuBk1x2EIEC2Ddx145tqHH19_QJ79lWmTrqhqcpfMroCSnEYfIglUPORTfjjgLPgJTbGzExCmPTL3YxKk9c-AbF94rIWvvAqaJHA1ld1zw5rSZV6Ycfs2EEZft-7TVTGGNO6s0NnhXzH_G_FoyryRz6219UuOzSwb0lA9PYnuqu6UdtAQFU9UsDfalOATGeYBMFcWVFs7nvrc5zzKU1QvQCiNKCdQGV4HLdBfoU84RTThru0Zz2SGzqB8GjQ5qqWmBls3m_j5HAukUzFnVp_IdyaZcX7cDyDjEs63QhmgOPAlbKMTOESpwfkT4-E_t0zi3mw9eRmJV181tjklAmnU4hQ7J_QqQsj9lPDGXuz27wLbWwhHrg81V6g916ATsjoq1EdelN7y_2rB8PduIQhAJDmnkUlPNsAX4XZ4Cua-yM0uudBmo0OSty8QXJIRc8DfOAdAmzEIodBnrCNoqVNb1pqkH06dxg0UysigcQ0IECMtr0rRWz-1KkzP2k0vOa8XL1QsPNHSAksPEXJL3Vj6WbXgNXuZSRLDmdKH_OeFP__c883n_YS_PQ8AVMrTyo3KLBTWEbX9IRnms3K9VpljKji5QhVz5xD7FLH5_Iwh_PIvQ8cBY_MtyTUyNXqWn8L7uL8GyyA1Ac8YHB5lMweMLY6JHufEMHXc1kaEOx5QgB7H8wxrFb8ziUFwC-wDgPS-xtVcH3D3lyOJbY9YIt1j-Xt8BySmFo3VctaH3YLRrFzhcsrg5rXkHUxyCxAXCQj2xZJIcWTvXfqeTf8p2K4qYOfBlf_0L2a3GRt9XO23d8vx-JuoYS3y1cL31fkieEb26Q52daOTW2yboPvyR06JdFojc_RoM4gLG1O6ulPbBHx4VfznWstCFGdpiUKFmKxCYiLTjzarDTgXPzrqwUf_05kptozE0En_8m8OxW71d_QXBbylwPjkaWBT7VB1hKJoPTGoou0UEciqdVx0uUKXYN1KHYA_Eb4awjGEne13seJu9lWTF20ZDSJIVGPe9QwVUP5ssjG9cVRP7MxxfcM5nKz-VzQxqjF-3-IV54BSKo6iRWSw6R3fIv_I7vpUIcfrEyH7GmfeDdJuxt3Z-WFQPdbTqv2wpjykH3fpXd4YL6kD3Bo5xtCLwnEGsZdFUGzzQqZkPO4NYEUKLbPdeauSVx9mcRVlW535hz9wOJDA7hsRyRmNkcbVc5TRN65Z2CCpDU_LTUwxf6jDjUnQ6qE3jmQ8i_PCD8FGIoKDNCWiE5ATl1IcmSMwyo3EBgPuYs2ijJ6Uj7ixMjfcbRpMCtdttYzNK0vYlP8C7-vUsoF92brqLqKz8c5wjiuAHL5CGzH5qrIZGsz1w4LOs-Hw32hstfcgLh1g5LnPDX2jXSP9Y9M52YoMQVTTTNKDU6XVn65D3yr4i1PYTPlRALTebuvrAZhlbsFpYaznkxrUGFC4ximCx33zeeP0fVCRxm3o9j5wwGS-up4pEd0qG8eHSsZb2zshZqBaBUzfhIzW6pSbaN_G5-2eBic5CCprSB1f6_IlSyppj0zc_3yAPTAi36yVRSQ5RvgEP_wCeJg2AySD514j3GY5Li5NWsJ3gRgMkbyyNkkKhAs28xmewLj-2FD7Fm8WhJ_hEXOSEvFpm-toVp-kyzfm_0AwsdmPI4nuqzs-FTuzVkVLAD2jC0g51v9cRk1HBIdCwRBqtnpipkfTlozroYAnuiUFKQzsBEBI5O5-_W-ZeLPpNkPp33TVUZZR3fba16a_RPe9ZBJFgDUxQSHHapab2is-fWskJYWH04bpVWauBC8Z5ew_usaBkqUOGTiozbmG2U9w7ptHz-UsggHi0ElbL-yO0rWLwfSIrQKdtT7V286W9lBiOBlyLHjxj6pndYDA3xpPDePBzcS1Y4lV7f4NK4B584BDS2TCUP4JtR9D_MBucppacWAj2RDd_OvRvK-RAdaZsrN7tUbD_Hg3L4wedpjWLHVx4Sb-tB4GKf2DuVg6AyR5IElbPwhWlBBYFM6gw6TnKEXZhBMSQBEGC-g6HLANDAMRAagDdm8jlL6VhNX3ehFaEifSd0r1_dGlBOYp9bR-A8k8KfPV8cfgK8kzMUYj_wyJ_2c7qfe8-WxPHPvbfG5HwQJYew6a7c1gJJ9P3ScMeENTO4I-jCVFI1c00xFx40GnLDw2sn3vydY7dFEG8sBzNsu5teau0XKe5c30SxSQFcfwk7P3UFqA9QbFjG54aE7-K3O8qkNHlCvayiNog3MeFqunOmCw7phwtRvHOxKqId-mRbDLX4EQhOZkv_vscsN5cBQwx6ek5i-fngRho2Kn5mvWUMzUrrCTwyMleI8SZjV3remksU5yhpsyWcOWVvYX7eFX3BtSryQ6EwZETaJozs3xCaZQH1DSt0Fwx9bxjAwQfmaR2n5I3xch7z_JF-F4doY6vv5M8_Sl5IWCLHfBaWbj_GdH-Y1pksXKSz3ZMor_vAqoR4-AZcfQznB4yYEwdo3VU-111IxZRJjsc6mwhC853DGfxUOUIiyIlYJtFzRHlyLmcYT6_EHFDENSwa2tVnj9T53AoJ5UHAPrrWxvkJ52l7nYuVFePjoiUOeSi36ekzyz6jkqAqx1ht4qGNKinHADzD2-O_T-10z2PzWST95gg-6Z5Py3t1M72Ob8okpUJCtdVI6ODTD6cm1ENewXOl9YqYtwdSJhDUW0SYaCwbNcwtQwjVHOdhUFmRygFaPj4Aci7PjJCAfUGZahXGyQ78pN-sIbhTukZsYKcXrqdR9Iz0UuJRqpdajYJcdhKbXnZH4J-v5V1SagZDQ0FqhMbHbr89fpouPdJRZO0-upu1qbf-P9F7UiahWtuWoGaU6r54fhW3UBqyA7VvRJhiHnhi7Jy51stFz4N--s5levgPhgXSQqda_sdRtWhUZ-PtkqXCwuJVZs-d2ectdDT_Pqgaw1VD9JvslLwywgye_fghTKCDPhmX_BUgMmRXDiKJDb1-Y_oyBJzVMrWWVJdciuaJLebVb7MotvQQguziTTOeFwPYK7D1bFGszz--H6tyzbnWv3vaJwq_JIIe6fGS9AjkAjoumT5mPjSA7kGTzDA7csnp4QnXV-Pb6N7UgMGSE--XBkMiDbHGsztCBFQbHUxIzCeXZecbRNVbEIhm2t786O1VtQC7ba3pMSFd-Hx0pcEkpoQk3Boog3suZ_EtSZrq-rTbZ95pxyEf7unG4MohEtqiCpfzJmuuCr3Zp_khGvdiZhHn0oHIx3HrQ10pS5tt75a598UewblVj_ywditRuNeOA13z6um7EBYVxgXrNG1ENSTBAx3CHL8blh7UD5LSPHgEYa3y7HQAU0IXVldb7Yx5UFSgfkFBfEGjQfVYxJY6vEj1aYY9LtavLFjfnT6s4nYCreUCG3i8aqCi9fuRKen1YyJudfa8drP5houPYjplwLTc2zMQZsu5gsWpIsQksCq-bn9MHvtq9bR30WeMizan2n6paLuWTmEEf3REc_D8jy9EOV_1huafTUPsHHvu0yAJDXHT38FHvpqcDX4BvB-21mYaIk65omnyUtmTijdCjHTk2DABzIHxkZiaPu-9c1RDO3zV8jnPpYy9qRgWfV9dor8svxv_Q02jW6NLUBDXA_8boFo0V_PSXvNlWTf3a4miffXE43YNEqDDbdIxc561IhaVWz6T20pnepPILAoeNED1F80SnHS6v-EB9o73qU-R-2T2Lq15Har6zOp835hrTy3inieh2kGknOdwJ8Thc4-tgOcye2U779sil5VZUJNe2sKASljpTh992_RteC5T_ISxRkEXkur4U6TvCrc3EYh2HYcnhtX7urqeYwKuidyBb3WHWyxdFg8hM3ucrTARoOeDFGzklgwCigvNnkMZfmIWj2QVMLVledwmvvHMSblWeZ2V5cPKDTb8eDCIJVUiUwz6qka2h8AiSSWK5KjQkT6HPlG2--IFSSd09jueC_KqLjrGPsIsllKIWWJ_wWGZqnJGXfWZFrPzUKA6YZCKnHjBa-GkO5Zy9awZX9jnDdtWGE0z7DHzW5vW5nBI9agZ3TDqUM6TL-Nutqdi30rJ6RM7A8SyQw6FaDd_NDjExLCWsNKe04kQE7_znWnhaFni1SLMls3r1Lguny4OWN8JV5ktZVbHrzdjx5WRW3zm_9QEVZciixeENHwuQB6xsOrdICi82UIXHH5oEDl6fMRnuozS-siOrfDxiLSoP9mu_j_865FVOgyHc1RIDkBytQNToP2Bj2f4GgcAuwWkqpjqavghqVhXQNcmawMxNfgqWTBfztZgpR_4KN5uWPN2p7i454HxKBtiTz9a-l4QWrP-2VOdOroTXDksM_XfqPe2XZphI8JMEmhnv5DDN96OGdASbj9-sfNw8SNCKjQELtB24Jc2q-TYVDbuPL1BX0xJQ3vpUJLQJMQCZtQaI8MSOAUA50qstui8KuvKqP0R8n8IWIxRUlb1nWHsXmshGehr2hDZDmk3RDwm4aLNhsh6eHJjaxIIQQIFJROnBT0qSST250El8963VHkoEEVRbkQZREFxOFLt1h0SJ0QvkXXX3YqJDJxFLiF_O7u4Uk_gjgouO3MMlJLEhYjxscMHZW3MjnXVXI3WnP-jzYnnw3SZpMB1EyMO5p5oNSPmgMxgR6BZUTDf5w7dwtkQpTvnFVpalI1g7wdRyEO2AStLzCwKC4AG9ZYFX20YsjchEekdLIeihbQTsOvV7RO1QF_TbPMeb6EYYsLpq5MVsgGVElbK8T_G-RvlV07H6KSB3kzhFpq3fFdwX12pJE7uQyTECPIfbb_g7Oh8AKYySq3IejmDFRjY_N8nyvlUoVGpKX6lbqtKHbqVaX92OomY3vCi8T1ilxl6CLMtFROsFj-hhUBWHyT4GaTIltIbp6TKCkQ9FbhbRyoeRjolFC-UPkKJ2suW8c1bhDhpAQ59OIdTdGKbFd1EEHpLvhsXCdIS1EzKmR6zzLrh0V3-snCbDlZ9wpLP3nooZ90-nvEdnUdaGMeXkBQn_xhHJGmrBVrj9Y39dxlGHdOIRbxuRb8X6EDTprgARsYR71O2U0NYQ7WDUyzA9xYCJVGwac97o4b7ELO-NEdzky8W3eHA8w57N-tbAdEqCFh7tCCC6V8tftmeT_X6Zcmoc_SuB34qHHiEXWIIGVSHg9U1OMeViPiZmh2n6w0khBLmRHCC1-qPnVGdNOIc19_Xx637UQbXzir3D99qJpFIPH5dYx8J0Qd1pjHM3ksCVhjxt9fSWlwmlqXurtyKl2UdXK1A8Q7_8IFQnkqt7dJIjGBmJhfmacweKFJxJmEEU0JW3zFUQmLIO5lC87wYtjMzYMgqySkUhw0_GeAkeutJ46tVY6y9U6c8U1MGu8oYanzP-69m6GjztrLQkG2XuweJ6FWwPDZrw1Zh23TijGK5JyUjmw3Cwubf1H9aVCZdxjsKryylW4jV6SVfoB0kQw1gGelJR4zZOj_qDiwII8neH2_gY-IDfd30LOOqykG8Lrj5TuX711cydSpXKiDV6IA_Igst4HX2vZNF3llXsezT3MIf3abM8Z250By0n0m5M0s2RD7k10_GOWCqcN1VW8jfcuk5kE90JW07k2pGy-bvum77gpA293CsnBbFnFD2FtjpkAwHHb-fUtd9UOIPxm2QcopkgvWEnRKkdMlqvr5FDqJw0IkNkp3BVpA5GN64MMH-EMVF7UmNsx7rggyqbEXEJCv75Xi-NGciJbjO0hFSE3eJTaANS5QnskJgMQb7WEaQo9OLpE6F6hY-M2b1c4c1W09dA3xX37vdH6KqUYTD3dklPEcDOR3pDJeylWhGDfeXJulILkkqzxHlFC3gJ4CIsOb_77aNG8qGkHAzUXwa_ZK8webasXSuNER-GQBFqgXxYaHXPLp3S2DeHO8gTV6T7UxbgK7Aw9H3DrTG2139bixQi-QIbMHA-rq6bQgEixYTonxNfjd9k5XnZti2hEHFBoskYIiDhkbq0hfklj5bqSTsTKgn-x9MQ6oUS4klBLTs96cM7KRv0D-qTKtw31LHmeEYq5HgmyVM6kwzCdK514hvYwDsyQTseo6bFwY7pXuA_O6-a2tRjVbq3l_-JdZTuFu95g5OgKWjP3qn6Mzef-WsG3N_tUaqlcaajOoRlSzBkfUARJ8Ge9NIOr0nN02LeIZKgWIIPIqx1kwtUKilO0cKDOHwo6q2uNDv-84LwsvXTPqCyM2LQpUOhnf2EkLbOtc6bEkqVqBAflYKVo36oXMBpnJBlwJTW4damz4DSb5wvnY8kp_oADNvTu5qrHu2ua46FZQTDkiCPNsoQYxL3Uwh-rW-9m5ROGRAHyI1_iQJ2Cw4SVbYDbw3ohbNgEIoOfNuhxKojFvz8yswlOkI6HYaNE5d3uCamuAvm88Wkop45_c5TGq6KABtZaXU5qvrhAxv9JbK4sblhcPU3NSRHkNBPDr9HD5R7GSpr9eue6zgWQvd4h-ipz6VT5RpEEbA78EtLUbVwCZFmb_s4zjlXvIXynxSBXv9tZuE4nPaN9Hqz9k7Mp9ja2PiwSt1dMESTdoT13CLGi2cXdLB_2437yMwKakomDTff8AYV8V3q9_owMht9rzIxcDg2OmgBKzwB2ebUt6jtVvEjWdl4vRvUTjVjAvnpz0UknpJ2unUNbDLvYnqOI2bKNxvomrNmVv-AlvTwZbWF6aKkVjPRIjCN_6LfkARoIa6bHrSPwX5nv2l_32SU7o_Q8u8G5NImtvHJMtNacQBPErpd_J2giW919pnemDEzNvn3jBv-RGksWttqeSOomn5dE3k9h8B61xKuLPgCsu3bypb5TXYkblWOLJVwRZTe8jJengFYTIWHiNSa3yJ4ANripgslp-HFsXeXI4nzvt7vCmvU2CtrkiNpvfoBLDnbu9aBTNMpXvxYf4eVXP9G1U7X3tgtEz2y-ACmE-chw-5UZz3KoSpVt-6yydRy4gTpbU6Fa6y1rvx5-Rpva8QYa7gIcN-33YnmMJzrKEdaL4spRhYhtKpAU-eyr0ePrsD0HajYCsaqMssNYjyTDduV_36DS_lKcpqVpvwatZl0EefB1mwjCPgV3DdBJVeFASuJRi1T4jH6VeQKdluIHfL5I40uujKEQmx3bktV_O25HN0xHpxy7KgQzk90D-_Qoqf3czzEVY9GuUqiyRpZs7VjQYdhLOufcRJvsPAw2_OxL0jb75UCUFMoqWuYwxCg6Tplwe8ZhydyjEqYS082WQdIYgge1ud4bnAJ5cuB8EQis6LF1DHJk-PChElZqr98cEHGh2e51blC21ankOz6rXO4yQpkilES0k9gJePvgGwm3nlyt1A2ZtC1VPFHm2N0hffiv8zqhX8vlPA99GpEQ-1FCKu1JLkZhWiq0NLn9m-5nrLe3VdlCFY1k_eVBjOz92AQU8Wln2iu9gdTBpxhjOsSnOH0niu1W7_-RppJ099tkfLvPRaP3otJ57WH2UIDU7RERPCKc--xEBwoTBR3ov9z2ypoeyKJBzAteJIZpCZOwUXIcHADVQYc2ZlwdZa3IBcUcFjxPlMh6Sq9K0A9mcVGmrHHVd3_OUP5rloEUkWESzfk5B0qmr-CCJu1O0BnYakW3wVLiQVs9JfCbP_cclcVpg6ajwKGmoB7uYDk0qphliylt4S5xJighf3IRE2P0kDrDSOb3jPnzsY6jLdkexSjFf73T0Czy5iUsh1HTd0GUmvCqDIoH-YxjC-ZtSwbIN6pyQJa5SuxyRPHBLGvC292w0MSgtiMgj8tDoH790mu8VkTQgUQUUm6nOvXXs82-7vuJ1yyhQBRy9Y82I4NUQrJooZqW1uE9UzpIYs8NoMlyg2sXevMXt3jFgClfekLz9vz6BiFaeoGIC7DRMvu2sqUesghvN66GOTFLPeuaWuWe21w7IP1uiK-YRyVNrqSKZkiMTLWW0cwpcKfCPrI1VFgX9r1LA8TgHVu1aC8zYaPKOJqBQhWDnK95Icdx91-gSEAPDddik3epgovgUAp5oz973Gx6jjJ7Mf4BxUT9xPsqUuDXs1Sk12bWtqYe7PVeC1_DuHBn_c2wFyYCneJPS4OeWHuEsnOlw_hdoRz3lIueUGBLikmHV_VKm5kO8hfxl-cF1lquCbWQ0CpGDwATXrD8jGNx5zk1K5PjN0fsLt_ZL6hR9uYDk2elOppxGYGB-_F23FQxF5qPqhn8hq0jglkEGzDzEsgjO1i7ansDxYwzmmBK1Hvv6emCJhS0TH00oXycJ2ptDcoJqgoo2n9g5MoM5JGffkDzJCzkftOtPYH2FpNR_thePAzUOrzghsG8aNEc3pRwgjtmXcRYRwLJqqVYng2-WX-2Sbhq3KAi_LDliG_TKLIKGg66JnNhfi5ANj4ARIA4yV_sBBxGtkXtGLOT6DjV9NGwKAuaT-njj4ON6moN7jHcfG9902J3Z-6M3_V07I97L1MkTxEwL6F4nddMC2uvyVnjFc-5MmNGUGcCy27fs2Fv8wroKelgm_nrBGkNLOWwQk9DfwgPUfFn8nXDSRGhRTz-jCScy1aW_HgzwCn1w3CZ7PNt3BiDGiwYP_dS6PgP-9YiMbuOdFnARipO6U3Ps58zl3RYJvjznrDidK6C4jlYk20_CWx005WlEZprt4ISawdV9P_AfYMLkSPwQDlSWb7VczB2fE-QMTMB3HxAyGf7eV_n2_IM4iLIb3mipNfAnUFhz2v3hqjIw9XNI0nWqjn9kkhqM7CxB0Q65JX634ugSDpy0mJD1UwLCMSnH3AH9MwITiUirf9jnvkTKMZZNHbyoO0DbBcd4gYwwGk2U049ZOFewPHucfgCd_7hfsgTgGNWCPhOnxJ8MLWGKUi3_-ZJuH4vrEQoI6uDpH3PMpST0qLCLw_HU1wihMShlNBr_07Of7gRjGlwTciMkn6qeNlKqhIx-8ZRK-r9y5zvnvVb94s6lUfGDtbLlx-w15KUcbSdnqOz6NKeDuUHOvJ6QD_yD8XdvH15WmSgkFnFT1T3xGwu4ibuJ6mgqPUUjhBmmCT-XmyYc4lBEgRa-M89pZ73Z8Gu18g5N76NKKp9ln82oKpDGkyoR5Nfa9yPYZ2UTkvI13lRXU8BxBh1rrOUL0HOr9IW5tAJExmkPPPO8HD7v7i2dVpE_KLNSCDWiPAkMkSx149pY95rGgMsJaXwqxVqCsN6Oo2NPTAnnUcR99h3Pz7ZsNsvA_JwJCvY4y9Rc4VSkbAxkWzE6HY5SkUuvwXiJlr86DXwy-6ilOtJ8pB_5LNofv0xKziWCZQMoj6bfi40y-e-oaTmNWMqzCmnEqvkNvNMkxIRG2yzwhXKRSWnEEFUQrT638St7YdvM3v_G1-XM3ZATf4HDovpHiRmxEArrU_dR5JPTlSyCHXyB28x6cv0NRrkyWUWfOz4kCXxa4co4gyotKEW3MIKZzUh1hFAGYeO_lZbTpSogM2tTLFKhZymYWUzKQgCi8zIhGQzo2MB0C9e8SeUm9cUV9louXBMs9ByvBZlAcIZP3GKQo6bfAHHhQn-POeeZFEPDxbKJHm20tidyPgpxT2gQy8IByxC30g1c_gPTFzZDaOrD-UTZzP5Yts5L2scKPzDWMlmxHU-9VN_pi1hkig-zDjOYnqB-TqVJzpLSn257HVLHLNt2_SE6z7QhGqofAF13uhmVglw_XqiEZ7-EvI6djsW_nSpqLbJpIyYLz_5Re1sgSmKjPxn8t5bSBgIW2b3odGMXnzDGGuoj524DsbSPmPSANkicDLI37SgBIlrX41NJYrACo6dkBcroEurb6A2Lo1RkNW5lN3Nvb1o8SizC9dUOXVT7MPQRlPmyy1sDF4CBFqeQoDjM8anCleMeFRtDE_MvmNT-IheUvKcND0cYmUewRWrr3oE1syMGawoCqzUUxUp69xxzLpN_xIlsOwkU2bAbt9hRQsKCT3LxMHIIhuk8K7QDrNroBmLLxXajKNLnKMvSD9C9tuinJRLH4EdaEI8MkCYgsN_YgWRXeKfCMgipTWxCx8q9L8bq3Q-IWdvGHXQGxkyJ7N9GSgCBtBX6VU5W5axkGAf6nRo-eDPhcc_aJKHNXS-tKGwXL7q_Y8ra8AF1c_nauwfxI0mjNCvO5S5sIuxO8Pb62PYUQYRdhN6lszrcCS8ALnleHjXZmwFO8i-sJe5OsIOvaGL7d2sf7innzBkqTUncG8s2gVTfqtmzzWtNKEwbFNookzDK8qeUMl-Z6k__IbygTIumMW0wu4E0zrxBFALBIoQRI2rV6SpYxjVs9PhEjEf4d0Wg4ZZXWHbDQIeIOax7uXimrt2THp2GZTYMPML3P_imbsmWSV9xK5OlqJ2Mkr49IjzO7vUGRAi6a-RPHIfUY-j6n6jK_MEbuKkqOVZO8n--7xec4OjWJdxzdz77XNPze7_Pgm0MXSaWTYui26azudv_6Mk_IIv3dtTJ-b9yeUGNpYAeO-V-InsSop7qUTZGMPOGwjj_qwVhkezryw_rNIMKJ66ugwGrJqmtb4ag7ZQwTHMRyKwuJUdUKurO09rkLNV0iav97Gagp4pKKBJfFNM8VKQtH8rewXIXjoysSOv5WpQbBW4diHxrbgZouafkxgMud4Durp8-0YlF8c1S2GzRgqtsBqQL64OW6v5P6CAms30Tf4LrlIO0DTAOH060TPk5tEXEn0agw2rHBhan-o89ti6qErizUMVS6d3Y5X5psRPysU6HvBarj8MYdiUXxYq61bK0Mg6lhJpcPL4JkBdTp0TVEvQ2wjSWWiep1LnVehq4f6okMOLS7vxyx2MdxTSghDFPVlXNmKLQXm7C9ogzSH7E6BRQmOBwGmT8dZhgp906wAzml9frlUN3LnREi8HQjFIMmPAsWM5g9BuWEmxS6HEnMAu0PuZkoQERsdRbWNUrIl6mAEfWASZdlTLiLmjOir42SSdlJbqzR2Er-wBmjh0clmysMjTphrURopsJOYTA26JTw8xqoWfWzM3GXi1B0iuWiSetTRjoL_OKtT46Gf8BTm-Q_kVJzJD7Y8dLhaNMROTtxanFxiLuV3VUb1Bz1zfvk0EN7uAZOTso1kUJWvr0be4DF80X3Jc2Oy3YYSvih-2Xhq8BSPxHndqKDmXQJKrB9O_mLe5kmmstwhHBAmSYuPyne12kibUM70tVMXIyVDhLJ10MaRnMi82VH-FGzMbsi8LRDfpTo35L1ZybD4ujyRvSijVmswFzTWU67O8ldzsbQwI9i5t0W2D6KBtuc9zxJWyQB7WgdICRUGBXVhPbm-X9vYPPFNbDWQNtDnPr9kM_kAy6WY33Kt9eBnx2FSFpQK0NE1AcrOk-0ruP5gdibznfeJLDT2g9XGXtoMSE55uGbwLCZqj54kmdhSS5BWBb7F0K-IKsftPO2K9bp7l8uW2Cb5mYxnlCPpvL-FdIs5JgGPRYwvmt_p8xOnRABTXj7XoHSYwwV2xFzxo5apapirUYp7z8Vf73eccnHzmOdRvcRqHHCZP3s8Yats9zJ_SbBGzQNlJrn5W1UvWRbiUYtAt-zSqDunC8ZHQIvzCfQQ1xIfS9LfA3cdS6R4ZPeY1e_kuZer4tutG0ivEYrOfBDaeDWnsT6Naht86N82VfLP5ShysS5zkDHn8xCQC5jqE_t9SEr0qLpbdHpZF6446KPoirnPmwOgdzdJoc_h2HCSTK4W9aoLD5m0qxPIuRzlJJUtapmenl5VI3wwmOUnBMl_Al9jNg6rdx4_KEgJU9rjCvf3dQAJrP1eOoL960MTd5jQYbBFznXRfX3BRFPwPS5-mnw6PLfGBCf9WwDXOSTVS_qvIiOEeMvT3bUxCSMZ5avuj3_-jB3EKCxDbVvUp0cvUL4IrrDByZROxMA2UW73LAvQ0X7UsOwoUtprRZc1lkO5eLh8sMEqZpVQi3_31D_ueTf7wYr8Vu4dWeusfRFIKUEmlyDn55txdK0cMeFzPtbzPR8T0bIcihvlf1P6eBk6re20xVaIbB3lqjlyAJYkj95PK8jRKEEl-IY5OOlKTSNlGC5uWTdZOUvsxouMMKeilV4M4O0yX5LKmB3JH7UzLfb4MOYwDKurrN1_utJl7QyYmkvUA9SUYxnfjtcCwA3Sg-Hap0GHirUgPYpmH5WRWDjVFympP3hIYk3hNzdHmL4CqjZL2J8fkQVCmz6tXzCHxkRgZIqmz0pJ33pp8EkxX1cyNgLFn-Pf7B0qaGPOhhn31vzOia9Nyj0Syw74bJG3IzBXB-GLZLQ2O5Vym7EBFWagvgBTYV8vtpYUhSZvM6GbWoResNUx9wJWh812FQVgvbUDO1cjF2f8LHPp02Y_PhKEA9Y7Ee9KPMn4mXIUo6rp0zuwTRtVwJUjIVK_kNnTiCBYiF2qHW_3ne68ZJMZajBkbYpjWV6N4K7PizrhBryspStDfeChsbexxbAVmq2if0afWFFUqQ7JYlSHozWJlB0w4hiF6tMWjiRq1QCYhYnAgKOVof-wc8pcU1bsYpLd2E0qz2tS2Eu9QjBDafpFqCE4LWgGVaJZyNl7Y289VMY-IGKHcYMBd4VB9R9NJA-kM78RQwT-djz9K8Xh7m5R8CL_YLYFEx8PRcZCulDW2WCYCN0kb16aSScjbBW3-MeIYSdmj4hMueb1PODGMFrcgyA2eOfn5SKRKoz78fdtag_luWqahBlNCCDbBnHBSEwoaDsZ0bAkUz02VtwDhcTgxjJ3wkz2DoYIZwnCLt3Erxw9_8L0P7KuXPRoLSYSzJzrv2igJguovUeE_ShGpD4mStiiUPkFFEdVkOZqPPvvWV9toy-n5qasnfiCxI8pnA-h02jtZJIvV4DkJZ4_6H_CEL-5N-tyQ1ULfwvHsmzRxjfYcQcmq7X3IgpGiXXfIH2bfOSRiHBzm8siMn_Yw8a8woO19mXIg2y9f1fPz_BHBzIs_Yp2D8JXCGvziS5Z6KbPROs6C8SuFfmAndZcuo9b7oVslndivBixr25c50CeYEtajdG9ar3c_-jr4-yOXrmj76nIoWWRkKBwGdD-JY45ZRFmXq_ZLMfFdgzNw9LfWsj-qLLvD-kI7YDqwO5izDyee6Kabf2U90c69eKl-3bdUBSzrHmUxT_wpwLGGfLOpdqf2dODbjCEtt3w_cAsld_1VTpxFKk9BTcYZKiG1TW-sHZjBiGh_1YGh1Y7soGp4IOi2ZXhIJT5rg2ZKnFhyGNwz75DHo8rmZspP4cPPLvixitsdt1LJFxykkeoX5KgwAqmWrgeC1DNuuH6MvL2CscoUZxaUJu-24s_Wr0JGE4LLUiYQvy6SNH0o9WHcTQhCGdJaYlxBlVfQ_b4ll_jPAZcMEwaJvlH0OfQyJ1kv5rEHF66_KXZ9EvHb5fX8T3y7_B80AwYH50ik779Vx_OCiXpnHSYxHaFeuqE_VYMvbEE6T3o2km8xTNCmm9EDAu3o_vuE3JQa6Q75_bewHiPjY4ZLxO61qG87qq6-59-avfRT4PEEwGvmKjyzSVpADV2Uj5d310Mf9E7TVm9vk9pvKmZogfvj48VKHyTtClct_XKWL6rWukZrylTP2-gueD7jMsUUkw_P3zuOuCiCVKqAUhaDBNi6aRQ3BUZ-n5-pGIbmdUbWg5VGANFzgOiPxRomghF2nAml1yqor-yUykB0KJd3yvoEH01bg1nmnTBXxsLWAGpD8mg7LYD75a0CDdYT1tOPuLJVa2reZVp4KkWnv0KhZndkbqGrOvutvgHKyqiO1hbeemUJlbPbQpTGDjOk-9eLkZLrUA4LHY2_3Ak9Xqs4WGsnB3zrZIT32DGmUeWO_dBgFEzn1QIOeYjR_9ApFjh7xE71C2VRj7HSmNBjaKbY5RArH23NxD7DDd1Wx_6Z7HrK436BIOgXB_LJg2Go9r0nQ14tb6WsWxhbx_KBlr0IVOYtnLpvniUnwupc12FJtD_xeuw_Y6Lha5rSzJknyk5QTmuA0aCmAFe4n6RvwiOAv0Ozn3VqnOQImYlMgyy7Wye41a02ncYSuSscQgx3V0roPvjhaY6WuDm2K7JFZADVHnP6bBQMaRcaUWrd3cbQV4IcKDWt-lUeyKSQKKoXTo8DyfMYMZhWG9QhwF6ZuG27F0x_kG-4G0PpIprUccgPafIeRmE6BG8KXqnULw4kGDltiUUQC37wYh1MkfAHR_9JlX_7fleYt1PEpBB69INMGy_w-QkReGTtiH2z6ALYgaQzdkabJQSQ-UYMyUqxWnP3_2sj1EDydjE2AetRMEbDpD61ytqLwGDfKxykmgHVIBKD6HRF0ztbeNbtqrw_ECRZItx0luL3fc2G0ynV13VzyTNQy7Qtl4gix2L9MD5aKR8Ggb7eFv3i9dQA6m9eJl977segNlBLlm7klurkKyFKoOctUVbH4B5wx06nfpHNjURHdDYQo_oB6mF9Uvh-yu9RxaD5dQeySFL1qlnTy6_6LA77NquoY0Yv92fuwETBMGz5E0_ifZDY0pgR3K-kUSfRUYRUCi7_4Xa_ZN6NKlhSOTD0bBW8Gp9cNh9458rOZ9UeSTY2OgNfNm-Wzf0HmYq1VWZ3R8kF6llpD8K9XUu3ItGHeIkag5IHVY1ijMJXqBibwRIboJxM0JOIm4_Rr5L-N9sfkFJFYY6Tq5odtQYjDPjOl2ZCrSjfHEHZDBxYljtDBGoBJFUeyWrkUwNlh59GPQSBX9BPRcq9gl2JNVe31MJxeke1iui-tKwDPHRCVftu-ZXb_cLv6QUmfP2Dyhx2ImwcIDL8Fp-2k6p9bKVepl7gZcm1bLIFvebdlJs_wqhL13eUlLPtvncQCXXoIh-RDP0z8S7cjhwJcQhhvwMn8qEkVKbjLbwI1WDQZy0wVU3jM1BM8zI33oekKacCQJyuGd2UOS4kuVLVw_ZqEfPlE_J-0sCrNWB8ejxScoGcZ0BDU_mN2UvQieiFZVHjkGwPsODquc87Zin_HuG2e77a7WBSecCegbBqdCNUrsurxc3qF2UtIKzoZuJeBn66Rzek-mKNFFbfom__3ZQo7f4PTKi3_nnYBdZhctoK1rlv5-iSfEgtw9PNKSeX59SpcI29_WuNHvCT2Zc-SVETABzYgoZuzyjP9Yp1SFv4_-fTRPEaY1uyp5D9goefRPul6LV2noycqZMni8hhe1xC6iIpMRNcCTJmbjSjJfwQNPFj7kqAU4BMrYelFsUK4VTSGDdEtiXWo7zjkcQEoBkOl7vrsSo4FGX85UPYad37dN3MLALfb5rhtk41ONMFekiYDuHoiu86y3Wlu_uvtchPiV9IJo7NAsza9Y62sj8oNlJMB91r32UJZyda-5evGQUqjRdny7EDd28mGK7Ame2K-uZ6BYe--9Xf3I1YuiHCQla9iHejPal6n2-fNt7FqpG9YSqFqalswfW1xYnd_AFcRXzG24K7H7VPRtCBE0inBZ75GP9UED5t3AYYdY6wuNj79V1Yfc748oQc2z01J1GgErILp1z7my9efM8F7cCq0nr7QZ-pxN6_qXGPmalwCT-C8vEGEA8Gn_L2pVZfMNs65oRyhgy9evWlBbM7BtUwFQ34MeIN8pdyJ7BKmt4FgselPuZy22KGzHcZ0-x2_4snheONJ2kZeHjO93cpDsVk_GHAQboJB0iMIl92BaUbG4ieQFhpGwKLfGEmWOuXpRJrFjalGyCoCOJOqbtMBtFtveOwPMtGPp_52kHXpdW3fxeqmb2JO_Edg39bacHTrcZ55NDYAbTyHptf9Q_9NS6g98jNosDV1u-iRvOR6LD7VpwhH4d5Arf4WY0UveSKVh5d3gcwEw5bQYkJlMLLY4zzRfNNgMwKqYImbdC7O2__rWzDi5Qgjnbq8xHfxPdixYG-VCpt35MobFW-6c2HPH1zJs6L9pgH1-b5gKl5DfTzqFHVmjN12nrm5CSADN1iYjc5oJLLKYnFKepifFrxF2g63k_Z9hMdvmaXmGNmrVAqOfK6j7nH49execjaIs5QTsTzI16rYIgVIoDhYfxh'
    return(str(num_decode(compressed)))