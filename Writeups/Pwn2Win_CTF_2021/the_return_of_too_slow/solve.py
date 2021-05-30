# Function to find lcs_algo
def lcs_algo(S1, S2, m, n):
	L = [[0 for x in range(n+1)] for x in range(m+1)]

	# Building the mtrix in bottom-up way
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif S1[i-1] == S2[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])

	index = L[m][n]

	lcs_algo = [""] * (index+1)
	lcs_algo[index] = ""

	i = m
	j = n
	while i > 0 and j > 0:

		if S1[i-1] == S2[j-1]:
			lcs_algo[index-1] = S1[i-1]
			i -= 1
			j -= 1
			index -= 1

		elif L[i-1][j] > L[i][j-1]:
			i -= 1
		else:
			j -= 1
			
	# Printing the sub sequences
	print("LCS: " + "".join(lcs_algo))

# data1
S2 = b'vYJ3,K*C=\\xkXo4t1HZldt1LR"3p*v,34*xdubE=03Hdw43*f2U3>xv0,9fTHB35f=onG\'lK\'H,VH3Z1=FM]7x9EUQ-,o<t3X${lB,6R1@<Ss $~9K[C%CwA{^zb}N9}zj.3a9=Zjbx3y.yP<\'8j.C.5p=xoC5H-05hvH\'\')Gv/y4 L%f9lRlE9xL_3:3reQK\'\'Vvn""v5L^,3"gb+7_3fbl#an#=Z,7Q$Q3,t#O$kZFJe# &gAmXRw;\\1>Xx_KXQX?4gPi=][vxvmafFSi=Lp(tB1C?4xMoFz*5[E*?hC?y_?H_HxRH31AisEF]_L"X9x3""ve"Xe_H!E$.v!.e!c\'!Lvc3e!*e*c81V%eT*"||" eCCQ/W3 rcc?zC CrH3G4/?G F|?I?-C?H1Gy ?"?G?$XK"#E]_f88p8nClS$9t*oV10"sG"9RH1G2*#91*4|2-9Ko3o>LR`oLo@i/@G@i!S)RTV.31bi#3Z;-<oo;NoS;NYY*o]Eox\\5p/}xvpVo)=k*Mo1o,KN>>xE>7DXo0oxwoL-cY0OilM#i-=MotMs,KR[+$K![**[O[c$5x)koc(o(o"C<3@@o;coZ?<V003vtl\'vbU4lv?oxx0_RPPA[.PPuh%%  M3n%*\'*4gx |x_9 $$tdF6vMubbo8;b3o_3LF0K#Vx3t3KhT:RKwwKM {3Fa,kMKMeou #_I3.Ib"Eiib*]@I1@@`;!kJtu!17_7]ZOoa4CR/l//BxuxQ2}m.otp4"BC$P.tPmioIyt3oY%y%{UaRo;UUyyU{H8:hKy;KQ]oo5:xdo\\((oK;7Ky>.kcJo-A %ic{{OoPor:o07;EM+C/k_7{H2YGTk:Dy%43Clv{ryyyXCC^o#{Y7>c\'s(bb7(c-o`$UWUYV.{,v% {{U-oaJ0.oc!nnJkvNkoMMvA?k1oM-;%oSMJE^o\\7;o,-iic-f!o/-Id ;YY!bk+]j3>-{\\M3onE3Is!{c;J{;JsngJtt _;E*MHot?-i-E1qiNhc{-kOMZ{ O{{{GZvBimE%eu77\'_3:pWc3```xerFK-wh63+0nYPaqG0}03!gGL2;I0 b>3%. 08w+" P<``ll333lpds+Q_+q>s{X;Cx!JZv\\O3|9d-;{{QD;Q}!!;3-HzMMDG-,|o>D!MM62@$i-TmK>~e!=yccv!9_v-d_v;=A`1v>axZy&;3y;Z  A.@<CG 4+sQo_o>z=<HCQ r_ 1,U(H}N32;;IEGy;Iy%FDe;kxh&kocKI(;:0__T3a-: ;I\\Ru3v r I)9bIK7K2bj12ms_<Go\\j rj_Do9.k HvM\\Dfq_{!>u/..a,c30vlU>u"|>E":;p@{M%iBkn_fW;jji>M[cVuuuI1S1\\0-Tv;c>:I\\T 1RDY=e777;!rsel_aTZMb0?ig0>w;F%k;l>0U/}1j;8;DXe0E@@sT!0.. NttOCc~k=`pnc>H>nm2`F|\\um`/K`{p/{T{?+*C`m~C >\'QnKnnwc@@}'.decode("latin-1")
# data2
S1 = b'D:P6B W@WUu`"cMiM`IWIVD(ILW;h.r&rIrG&IzOhii`O`|NqO66XA%G`~SC[!&i+T[?;IgT`gIS& 8|`<aa_6mq76cD((]&I&s//+/8MPS+#`r_DTJ6q}Dc)){I{FFPcX(y-JjOkN\'}Bw|k:wV`Rt0r{:yx2>P#Yqb(!eka\\$#bq|^Inn%DbyuY~z{Q~_>qc|\\D&rrW^~SecD@f*%RDv]h_ :(@:Rd:)]D>fjpydId:O#J0::IlCkD(fcp;q(+a")gD_ J!jj@i\\q\\ ht}^s-Q_6{ij*z#s<bYV.zS_v;iIr))iQawWAResmWA@U:NNln8<AUgc2RrO<Z>\\5%ZqA2eZ;Y0;OD8(OAZo:68jg`rUqD-jQ7OQ@|m7eJ`AhJe=J=k`=wu2e:]Pdd5X~bAeP4J@Yh#ej(O5eeJwjD6J~`r>jjV`j$9my\\.}&j\\D_,D,q\\j+)Drr)lI+qwDMIYNoo6YurFkj(P&o&OnDENqKm8M&^U]qrq6wg~|w%[~\'ooYoD^oqjP%oo?&oooWZ6ZqtdedUtoBfG^s^reo\'eO<boCdG~o`b^uJfPoooq|m%D.onEqo2~WJ~)qK-,Enj)~~B~B)1~!oF~6njDDWg,TcH+ri^gnpnVqI5Vq_w8U~&5r5&j25I6z(&tqWJ_X0:ToSW_tSdW<a\'&Dk6~hhh2/eV_^ODg7<tgoJ~o~zq9<S~=j<AjqFz@3VoN=V~So^+o6=<=mm^<[SoS66o|=+Zw!m+~moZ`o+W#*)j|6pXfh)"hhq8)L~|LLj4I4WL[6oL$o8jW|$j7qoj[N[IN9o~,_sS,f),f~f~i~).)B>$}l+omS}|wmoGmjoo1zoz+zdFFIzo/@otro]r&gpz&"kFB88/6559"/Kz&pozo)|u6X|8Nu66ou&P4U<<o)?vnG$m&`mPzzzgj@Y\\45W\\4W466<UuL_DBjTWS5w9WS]8&ti9Wnxff$9pSA`CT8[SS0)8WF)4WFVL55\'@m\'4t&nm#L6eppGDSj|x_Sp]aSeG]~Fy\'[1a_j5m/f99OkHO~\'~"%Y/&HfH)H)igrR6gR\\!hq~q?=~Zahah^immJrrSXVQyMxp~s#~jFN~r.r*Rz}R_??dKed^)m^^RT"steAS)([oe*(m%*]mh#d#swPPYqqqWE#eeS-#5#rr_dpS[#lS?RfaL5OHFWtBO[~#L@^]a]X@ym)atH)Qa(sY*"**bR_Uobvhhg"Z[\'#ru"]2_V)LbfL6e]]e~\'Rr~d\'MW##W:]]]^8:5^^ckYyzze$d,WLOg)iaJ$+n\'B@[r=r\']C#]DOZE.$LBo55zsBX&h/F[_45dQOpfsso^`^"O=kN**5U8)z6,R4)wr&*##gr5gzR#xgBRBRY+{1]_y2YuVnFiOt)5NF^l]&FYY#x\'579LGs3]vPP(A^(6e<2a56CeflrO55Jbse:fE#$5AU7DI$#$Z}Z*$PUZ[J,W_*4qy|}YvfAkNL}49"aL!dRh-h%g5oV[eRJW[Add<L9$xJ}'.decode("latin-1")

m = len(S1)
n = len(S2)
lcs_algo(S1, S2, m, n)
