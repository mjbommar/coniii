# MIT License
# 
# Copyright (c) 2017 Edward D. Lee, Bryan C. Daniels
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Equations for 4-spin Ising model.

# Written on 2018/12/12.
from numpy import zeros, exp, array, prod, isnan
from scipy.special import logsumexp

def calc_observables(params):
    """
    Give each set of parameters concatenated into one array.
    """
    Cout = zeros((10))
    H = params[0:4]
    J = params[4:10]
    energyTerms = [    +0, +H[3]+0, +H[2]+0, +H[2]+H[3]+J[5], +H[1]+0, +H[1]+H[3]+J[4], +H[1]+H[2]+J[3], +H[1]+H[2]+H[3]+J[3]+
    J[4]+J[5], +H[0]+0, +H[0]+H[3]+J[2], +H[0]+H[2]+J[1], +H[0]+H[2]+H[3]+J[1]+J[2]+J[5], +H[0]+H[1]+J[0], +
    H[0]+H[1]+H[3]+J[0]+J[2]+J[4], +H[0]+H[1]+H[2]+J[0]+J[1]+J[3], +H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+
            J[4]+J[5],]
    logZ = logsumexp(energyTerms)
    num = logsumexp(energyTerms, b=[0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1], return_sign=True)
    Cout[0] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1], return_sign=True)
    Cout[1] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1], return_sign=True)
    Cout[2] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1], return_sign=True)
    Cout[3] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1], return_sign=True)
    Cout[4] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1], return_sign=True)
    Cout[5] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1], return_sign=True)
    Cout[6] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1], return_sign=True)
    Cout[7] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1], return_sign=True)
    Cout[8] = exp( num[0] - logZ ) * num[1]
    num = logsumexp(energyTerms, b=[0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1], return_sign=True)
    Cout[9] = exp( num[0] - logZ ) * num[1]
    Cout[isnan(Cout)] = 0.
    return(Cout)

def p(params):
    """
    Give each set of parameters concatenated into one array.
    """
    Cout = zeros((10))
    H = params[0:4]
    J = params[4:10]
    H = params[0:4]
    J = params[4:10]
    Pout = zeros((16))
    energyTerms = [    +0, +H[3]+0, +H[2]+0, +H[2]+H[3]+J[5], +H[1]+0, +H[1]+H[3]+J[4], +H[1]+H[2]+J[3], +H[1]+H[2]+H[3]+J[3]+
    J[4]+J[5], +H[0]+0, +H[0]+H[3]+J[2], +H[0]+H[2]+J[1], +H[0]+H[2]+H[3]+J[1]+J[2]+J[5], +H[0]+H[1]+J[0], +
    H[0]+H[1]+H[3]+J[0]+J[2]+J[4], +H[0]+H[1]+H[2]+J[0]+J[1]+J[3], +H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+
            J[4]+J[5],]
    logZ = logsumexp(energyTerms)
    Pout[0] = exp( +0 - logZ )
    Pout[1] = exp( +H[3]+0 - logZ )
    Pout[2] = exp( +H[2]+0 - logZ )
    Pout[3] = exp( +H[2]+H[3]+J[5] - logZ )
    Pout[4] = exp( +H[1]+0 - logZ )
    Pout[5] = exp( +H[1]+H[3]+J[4] - logZ )
    Pout[6] = exp( +H[1]+H[2]+J[3] - logZ )
    Pout[7] = exp( +H[1]+H[2]+H[3]+J[3]+J[4]+J[5] - logZ )
    Pout[8] = exp( +H[0]+0 - logZ )
    Pout[9] = exp( +H[0]+H[3]+J[2] - logZ )
    Pout[10] = exp( +H[0]+H[2]+J[1] - logZ )
    Pout[11] = exp( +H[0]+H[2]+H[3]+J[1]+J[2]+J[5] - logZ )
    Pout[12] = exp( +H[0]+H[1]+J[0] - logZ )
    Pout[13] = exp( +H[0]+H[1]+H[3]+J[0]+J[2]+J[4] - logZ )
    Pout[14] = exp( +H[0]+H[1]+H[2]+J[0]+J[1]+J[3] - logZ )
    Pout[15] = exp( +H[0]+H[1]+H[2]+H[3]+J[0]+J[1]+J[2]+J[3]+J[4]+J[5] - logZ )

    return(Pout)
