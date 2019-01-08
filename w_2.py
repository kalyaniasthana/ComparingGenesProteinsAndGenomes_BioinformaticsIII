# -*- coding: utf-8 -*-
from __future__ import print_function
import copy
from w_1 import *

blosum62 = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}
indel_penalty = -5
def GlobalAlignment(v, w):
	s = []
	backtrack = []
	p = len(v)
	q = len(w)
	s = [[0 for x in xrange(q+1)] for x in xrange(p+1)] 
	for i in range(0, p + 1):
		for j in range(0, q + 1):
			if i == 0 or j == 0: 
				if i == 0 and j == 0:
					s[i][j] = 0
				elif i == j or i > j:
					s[i][j] = i*indel_penalty
				elif i < j:
					s[i][j] = j*indel_penalty
			else: 
				s[i][j] = max(s[i-1][j-1] + blosum62[v[i-1]][w[j-1]], s[i-1][j] + indel_penalty, s[i][j-1] + indel_penalty)
				
	k = []
	l = []
	i = len(v)
	j = len(w)
	while i > 0 and j > 0:
		if s[i][j] == s[i-1][j-1] + blosum62[v[i-1]][w[j-1]]: 
			k.append(v[i-1])
			l.append(w[j-1])
			i -= 1
			j -= 1
		elif s[i][j] == s[i-1][j] + indel_penalty:
			k.append(v[i-1])
			l.append('-')
			i -= 1
		elif s[i][j] == s[i][j-1] + indel_penalty:
			k.append('-')
			l.append(w[j-1])
			j -= 1

	while i > 0:
		k.append(v[i-1])
		l.append('-')
		i -= 1
	while j > 0:
		k.append('-')
		j.append(w[j-1])
		j -= 1

	k = ''.join(k[::-1])
	l = ''.join(l[::-1])
	print(s[p][q])
	print(k)
	print(l)
	return None

v = 'CPRIPMSPAPKLCQQWMESPIDYLYVGLFCREEATHSRPHEGEVLWRKMREFDIKIGIRRCVTFYMHGGSPQIWVFWTDILSRLWPNYPANVPTIRATITYHALLYTECIGFEKIAEQTGQFLLGFIIHNVYWQMHFNHVRLYRPEQEDPLRQEDSKDTPCIGTVCVKYKSQSPTLKHHEKHYNKNVAYVTMFFMHSSGNGTIPPGYETVSWLAGGEGRWRNKLVCTQANAHIPHVGCELMLCRQGGTLYAFAYAQCDGSPPCDVMPMGMHQIDILFEFTNQYTETWDLMNAPCLDSMSLVRWKPLCYAGDGTWMVKFPSHINVCYKPFVLALIHMCSNGVKMGWKLCEILLNFYYGFKSEHRETWRACPWKWHRNLPESTAFMLYMVALFCTMFTFMECPTYDMAFFRTGGSTDNSTLSATQWMDHWEMSRYFWSRGLSMLRVEWGADCIHAVMLMPSITNIQYANNHGSLCATVNKLNQRQPMEHHWLHRSTYKQIQHFPERNTALVWNSLAMLNAPISWDTIKVCPSKPCPWFPTFLWTVWWDLLWAWPGTSIYFYLSAYGQMCISLWMQDPTDKEKHRERNNYRNQQHWQFAFQLDLASSTIDPNLQENPDSNKWRYARRVPWCSHKCNFLIAAVNVWAMMWIFGEDAQVATFMNSYYVTMHGCMFKYVIQFQKQRMEHAKVKRVTVLKKRFMCYFMLCHCSHWVVGEDSKGPGHYCTLYQYNAIQVCWMLYYEWRLIQDDMAPPHPEMWMVGNHNHSENAGKMAVKNTNAYNGHYIMAHNGEQDIVVIETYWTHANSCPFYRQLIELHPYKIQSIHCVVAWFL'
w = 'KPGIPMSPAPKICQYDCTKLHVGLFAREEATHSRPCFVRENEVCWRKMREFDIKIGIRRCVTFYMEAEVWGGSPQIWVYNQMFWTCILNYLWPNYPAFVPTSRATITYHAPEKIAEQSGQFSLVFRLYRPCQEDPLRSLYSWQGPIPTLWCVKYKSQSPTVNKLILNIKHHETHYNKPHVAYVTMFAMMRVCAIPPGYEVGRWRNKLVCTQALAHIPHVGMELMLGGGTLYAFAYLQSANGGHQCDGSPPCDVFQIDIQAQTGLPTNHYTEAWDPCLDSCYAGDGTWMAKFPSHILALIHMCSNNPVKMGWKQCEILFNFYLMKHPWKWDTAMLYMVALFCFTFMEFKMWHSQTAGNSGRPIRSLELSFTQWMDHWEMHRDFSNHARYFWCKMCKSLGLSMLRPEWGADCIHAVMNMHITSSGFLTNIGSYCYKLVNKLNQRQPMEHHDITFCLSTYKQITALVWFKWGENKKTICVCPSKVCPWFQTFLWTVWWKLLWAWPGGSIYFYLSAYGQMCISLWMTDKETRHRERNKFHACNYRNQQHSSTIDPNLNPDSNKWHHARRVPWCSVTANQCPWYFCDLLWASCVPAMMWMFGEDARLHAVATFMNSYYFNVTHHGCMFIICVKYMEHAKVKESKGVTVLKKRFMCHCFHWVVGEENASKGPGHYCTLYAAIQVCWMLYYEWPPRLIQDDGHCANVKGNHNHSENGGKMAGKNTNAYNAHNGWAHQDVIETYWTHKNSQSLHPYKYQSIHTVVAWFG'

print(GlobalAlignment(v, w))

