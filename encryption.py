__all__ = ['test']
# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)


def setVar(mod, exp, password):
    varDict = {"mod": mod, "exp": exp, "password": password}
    return varDict


def runStuff(varDict):
    # Code follows:
    var.registers(['bnpAddTo', 'bnpInvDigit', 'bnpMultiplyLowerTo', 'bnTestBit', 'bnGCD', 'bnpFromRadix', 'BigInteger', 'montReduce', 'cRevert', 'bnShortValue', 'bnEquals', 'bnOr', 'lplim', 'bnpCopyTo', 'Barrett', 'bnMod', 'bnpSquareTo', 'bnAdd', 'op_andnot', 'bnMultiply', 'Classic', 'pubKey', 'exponent', 'int2char', 'am1', 'BI_RM', 'bnDivide', 'bnAndNot', 'op_and', 'nbits', 'bnpMultiplyUpperTo', 'bnSigNum', 'RSAPublicKey', 'intAt', 'bnNegate', 'bnpMultiplyTo', 'nbi', 'j_lm', 'bnpIsEven', 'bnpMillerRabin', 'bnClearBit', 'encryptedPassword', 'cConvert', 'username', 'bnShiftRight', 'bnpChunkSize', 'bnpDivRemTo', 'RSA', 'bnFlipBit', 'am3', 'montMulTo', 'bnpFromInt', 'canary', 'Base64', 'bnpBitwiseTo', 'bnpFromNumber', 'bnpClamp', 'password', 'bnBitLength', 'montConvert', 'bnToByteArray', 'bnpRShiftTo', 'nbv', 'bnAnd', 'barrettConvert', 'bnIsProbablePrime', 'op_or', 'rr', 'bnClone', 'bnpDRShiftTo', 'dbits', 'am2', 'bnToString', 'bnpModInt', 'bnModInverse', 'bnShiftLeft', 'nSqrTo', 'bnNot', 'bnSubtract', 'bnDivideAndRemainder', 'bnpDAddOffset', 'bnGetLowestSetBit', 'bnAbs', 'bnCompareTo', 'bnMax', 'bnpDLShiftTo', 'vv', 'bnpDMultiply', 'op_xor', 'bnRemainder', 'montRevert', 'cbit', 'NullExp', 'bnMin', 'Hex', 'bnXor', 'barrettMulTo', 'lbit', 'cMulTo', 'Montgomery', 'BI_RC', 'bnpChangeBit', 'bnpExp', 'bnpSubTo', 'nNop', 'nMulTo', 'bnSetBit', 'cSqrTo', 'barrettSqrTo', 'bnpFromString', 'lowprimes', 'modulus', 'cReduce', 'bnModPowInt', 'bnByteValue', 'bnpLShiftTo', 'bnpToRadix', 'barrettReduce', 'bnPow', 'bnBitCount', 'montSqrTo', 'barrettRevert', 'bnIntValue', 'bnModPow', 'BI_FP'])
    @Js
    def PyJsHoisted_BigInteger_(a, b, c, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
        var.registers(['b', 'c', 'a'])
        if (var.get('a')!=var.get(u"null")):
            if (Js('number')==var.get('a',throw=False).typeof()):
                var.get(u"this").callprop('fromNumber', var.get('a'), var.get('b'), var.get('c'))
            else:
                if ((var.get('b')==var.get(u"null")) and (Js('string')!=var.get('a',throw=False).typeof())):
                    var.get(u"this").callprop('fromString', var.get('a'), Js(256.0))
                else:
                    var.get(u"this").callprop('fromString', var.get('a'), var.get('b'))
    PyJsHoisted_BigInteger_.func_name = 'BigInteger'
    var.put('BigInteger', PyJsHoisted_BigInteger_)
    @Js
    def PyJsHoisted_nbi_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('BigInteger').create(var.get(u"null"))
    PyJsHoisted_nbi_.func_name = 'nbi'
    var.put('nbi', PyJsHoisted_nbi_)
    @Js
    def PyJsHoisted_am1_(i, x, w, j, c, n, this, arguments, var=var):
        var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['j', 'v', 'n', 'w', 'i', 'c', 'x'])
        while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
            var.put('v', (((var.get('x')*var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))+var.get('w').get(var.get('j')))+var.get('c')))
            var.put('c', var.get('Math').callprop('floor', (var.get('v')/Js(67108864))))
            var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('v')&Js(67108863)))
        return var.get('c')
    PyJsHoisted_am1_.func_name = 'am1'
    var.put('am1', PyJsHoisted_am1_)
    @Js
    def PyJsHoisted_am2_(i, x, w, j, c, n, this, arguments, var=var):
        var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['j', 'n', 'w', 'i', 'l', 'xh', 'xl', 'm', 'c', 'x', 'h'])
        var.put('xl', (var.get('x')&Js(32767)))
        var.put('xh', (var.get('x')>>Js(15.0)))
        while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
            var.put('l', (var.get(u"this").get(var.get('i'))&Js(32767)))
            var.put('h', (var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))>>Js(15.0)))
            var.put('m', ((var.get('xh')*var.get('l'))+(var.get('h')*var.get('xl'))))
            var.put('l', ((((var.get('xl')*var.get('l'))+((var.get('m')&Js(32767))<<Js(15.0)))+var.get('w').get(var.get('j')))+(var.get('c')&Js(1073741823))))
            var.put('c', (((PyJsBshift(var.get('l'),Js(30.0))+PyJsBshift(var.get('m'),Js(15.0)))+(var.get('xh')*var.get('h')))+PyJsBshift(var.get('c'),Js(30.0))))
            var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('l')&Js(1073741823)))
        return var.get('c')
    PyJsHoisted_am2_.func_name = 'am2'
    var.put('am2', PyJsHoisted_am2_)
    @Js
    def PyJsHoisted_am3_(i, x, w, j, c, n, this, arguments, var=var):
        var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['j', 'n', 'w', 'i', 'l', 'xh', 'xl', 'm', 'c', 'x', 'h'])
        var.put('xl', (var.get('x')&Js(16383)))
        var.put('xh', (var.get('x')>>Js(14.0)))
        while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
            var.put('l', (var.get(u"this").get(var.get('i'))&Js(16383)))
            var.put('h', (var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))>>Js(14.0)))
            var.put('m', ((var.get('xh')*var.get('l'))+(var.get('h')*var.get('xl'))))
            var.put('l', ((((var.get('xl')*var.get('l'))+((var.get('m')&Js(16383))<<Js(14.0)))+var.get('w').get(var.get('j')))+var.get('c')))
            var.put('c', (((var.get('l')>>Js(28.0))+(var.get('m')>>Js(14.0)))+(var.get('xh')*var.get('h'))))
            var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('l')&Js(268435455)))
        return var.get('c')
    PyJsHoisted_am3_.func_name = 'am3'
    var.put('am3', PyJsHoisted_am3_)
    @Js
    def PyJsHoisted_int2char_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get('BI_RM').callprop('charAt', var.get('n'))
    PyJsHoisted_int2char_.func_name = 'int2char'
    var.put('int2char', PyJsHoisted_int2char_)
    @Js
    def PyJsHoisted_intAt_(s, i, this, arguments, var=var):
        var = Scope({'s':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['s', 'c', 'i'])
        var.put('c', var.get('BI_RC').get(var.get('s').callprop('charCodeAt', var.get('i'))))
        return ((-Js(1.0)) if (var.get('c')==var.get(u"null")) else var.get('c'))
    PyJsHoisted_intAt_.func_name = 'intAt'
    var.put('intAt', PyJsHoisted_intAt_)
    @Js
    def PyJsHoisted_bnpCopyTo_(r, this, arguments, var=var):
        var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'r'])
        #for JS loop
        var.put('i', (var.get(u"this").get('t')-Js(1.0)))
        while (var.get('i')>=Js(0.0)):
            try:
                var.get('r').put(var.get('i'), var.get(u"this").get(var.get('i')))
            finally:
                    var.put('i',Js(var.get('i').to_number())-Js(1))
        var.get('r').put('t', var.get(u"this").get('t'))
        var.get('r').put('s', var.get(u"this").get('s'))
    PyJsHoisted_bnpCopyTo_.func_name = 'bnpCopyTo'
    var.put('bnpCopyTo', PyJsHoisted_bnpCopyTo_)
    @Js
    def PyJsHoisted_bnpFromInt_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x'])
        var.get(u"this").put('t', Js(1.0))
        var.get(u"this").put('s', ((-Js(1.0)) if (var.get('x')<Js(0.0)) else Js(0.0)))
        if (var.get('x')>Js(0.0)):
            var.get(u"this").put('0', var.get('x'))
        else:
            if (var.get('x')<(-Js(1.0))):
                var.get(u"this").put('0', (var.get('x')+var.get('DV')))
            else:
                var.get(u"this").put('t', Js(0.0))
    PyJsHoisted_bnpFromInt_.func_name = 'bnpFromInt'
    var.put('bnpFromInt', PyJsHoisted_bnpFromInt_)
    @Js
    def PyJsHoisted_nbv_(i, this, arguments, var=var):
        var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'r'])
        var.put('r', var.get('nbi')())
        var.get('r').callprop('fromInt', var.get('i'))
        return var.get('r')
    PyJsHoisted_nbv_.func_name = 'nbv'
    var.put('nbv', PyJsHoisted_nbv_)
    @Js
    def PyJsHoisted_bnpFromString_(s, b, this, arguments, var=var):
        var = Scope({'s':s, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['k', 's', 'b', 'sh', 'i', 'mi', 'x'])
        pass
        if (var.get('b')==Js(16.0)):
            var.put('k', Js(4.0))
        else:
            if (var.get('b')==Js(8.0)):
                var.put('k', Js(3.0))
            else:
                if (var.get('b')==Js(256.0)):
                    var.put('k', Js(8.0))
                else:
                    if (var.get('b')==Js(2.0)):
                        var.put('k', Js(1.0))
                    else:
                        if (var.get('b')==Js(32.0)):
                            var.put('k', Js(5.0))
                        else:
                            if (var.get('b')==Js(4.0)):
                                var.put('k', Js(2.0))
                            else:
                                var.get(u"this").callprop('fromRadix', var.get('s'), var.get('b'))
                                return var.get('undefined')
        var.get(u"this").put('t', Js(0.0))
        var.get(u"this").put('s', Js(0.0))
        var.put('i', var.get('s').get('length'))
        var.put('mi', Js(False))
        var.put('sh', Js(0.0))
        while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
            var.put('x', ((var.get('s').get(var.get('i'))&Js(255)) if (var.get('k')==Js(8.0)) else var.get('intAt')(var.get('s'), var.get('i'))))
            if (var.get('x')<Js(0.0)):
                if (var.get('s').callprop('charAt', var.get('i'))==Js('-')):
                    var.put('mi', Js(True))
                continue
            var.put('mi', Js(False))
            if (var.get('sh')==Js(0.0)):
                var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), var.get('x'))
            else:
                if ((var.get('sh')+var.get('k'))>var.get(u"this").get('DB')):
                    var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), ((var.get('x')&((Js(1.0)<<(var.get(u"this").get('DB')-var.get('sh')))-Js(1.0)))<<var.get('sh')), '|')
                    var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), (var.get('x')>>(var.get(u"this").get('DB')-var.get('sh'))))
                else:
                    var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (var.get('x')<<var.get('sh')), '|')
            var.put('sh', var.get('k'), '+')
            if (var.get('sh')>=var.get(u"this").get('DB')):
                var.put('sh', var.get(u"this").get('DB'), '-')
        if ((var.get('k')==Js(8.0)) and ((var.get('s').get('0')&Js(128))!=Js(0.0))):
            var.get(u"this").put('s', (-Js(1.0)))
            if (var.get('sh')>Js(0.0)):
                var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (((Js(1.0)<<(var.get(u"this").get('DB')-var.get('sh')))-Js(1.0))<<var.get('sh')), '|')
        var.get(u"this").callprop('clamp')
        if var.get('mi'):
            var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get(u"this"))
    PyJsHoisted_bnpFromString_.func_name = 'bnpFromString'
    var.put('bnpFromString', PyJsHoisted_bnpFromString_)
    @Js
    def PyJsHoisted_bnpClamp_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['c'])
        var.put('c', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
        while ((var.get(u"this").get('t')>Js(0.0)) and (var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))==var.get('c'))):
            var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())-Js(1))
    PyJsHoisted_bnpClamp_.func_name = 'bnpClamp'
    var.put('bnpClamp', PyJsHoisted_bnpClamp_)
    @Js
    def PyJsHoisted_bnToString_(b, this, arguments, var=var):
        var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['k', 'd', 'b', 'p', 'r', 'km', 'i', 'm'])
        if (var.get(u"this").get('s')<Js(0.0)):
            return (Js('-')+var.get(u"this").callprop('negate').callprop('toString', var.get('b')))
        pass
        if (var.get('b')==Js(16.0)):
            var.put('k', Js(4.0))
        else:
            if (var.get('b')==Js(8.0)):
                var.put('k', Js(3.0))
            else:
                if (var.get('b')==Js(2.0)):
                    var.put('k', Js(1.0))
                else:
                    if (var.get('b')==Js(32.0)):
                        var.put('k', Js(5.0))
                    else:
                        if (var.get('b')==Js(4.0)):
                            var.put('k', Js(2.0))
                        else:
                            return var.get(u"this").callprop('toRadix', var.get('b'))
        var.put('km', ((Js(1.0)<<var.get('k'))-Js(1.0)))
        var.put('m', Js(False))
        var.put('r', Js(''))
        var.put('i', var.get(u"this").get('t'))
        var.put('p', (var.get(u"this").get('DB')-((var.get('i')*var.get(u"this").get('DB'))%var.get('k'))))
        if ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
            if ((var.get('p')<var.get(u"this").get('DB')) and (var.put('d', (var.get(u"this").get(var.get('i'))>>var.get('p')))>Js(0.0))):
                var.put('m', Js(True))
                var.put('r', var.get('int2char')(var.get('d')))
            while (var.get('i')>=Js(0.0)):
                if (var.get('p')<var.get('k')):
                    var.put('d', ((var.get(u"this").get(var.get('i'))&((Js(1.0)<<var.get('p'))-Js(1.0)))<<(var.get('k')-var.get('p'))))
                    var.put('d', (var.get(u"this").get(var.put('i',Js(var.get('i').to_number())-Js(1)))>>var.put('p', (var.get(u"this").get('DB')-var.get('k')), '+')), '|')
                else:
                    var.put('d', ((var.get(u"this").get(var.get('i'))>>var.put('p', var.get('k'), '-'))&var.get('km')))
                    if (var.get('p')<=Js(0.0)):
                        var.put('p', var.get(u"this").get('DB'), '+')
                        var.put('i',Js(var.get('i').to_number())-Js(1))
                if (var.get('d')>Js(0.0)):
                    var.put('m', Js(True))
                if var.get('m'):
                    var.put('r', var.get('int2char')(var.get('d')), '+')
        return (var.get('r') if var.get('m') else Js('0'))
    PyJsHoisted_bnToString_.func_name = 'bnToString'
    var.put('bnToString', PyJsHoisted_bnToString_)
    @Js
    def PyJsHoisted_bnNegate_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['r'])
        var.put('r', var.get('nbi')())
        var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnNegate_.func_name = 'bnNegate'
    var.put('bnNegate', PyJsHoisted_bnNegate_)
    @Js
    def PyJsHoisted_bnAbs_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (var.get(u"this").callprop('negate') if (var.get(u"this").get('s')<Js(0.0)) else var.get(u"this"))
    PyJsHoisted_bnAbs_.func_name = 'bnAbs'
    var.put('bnAbs', PyJsHoisted_bnAbs_)
    @Js
    def PyJsHoisted_bnCompareTo_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'i', 'r'])
        var.put('r', (var.get(u"this").get('s')-var.get('a').get('s')))
        if (var.get('r')!=Js(0.0)):
            return var.get('r')
        var.put('i', var.get(u"this").get('t'))
        var.put('r', (var.get('i')-var.get('a').get('t')))
        if (var.get('r')!=Js(0.0)):
            return var.get('r')
        while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
            if (var.put('r', (var.get(u"this").get(var.get('i'))-var.get('a').get(var.get('i'))))!=Js(0.0)):
                return var.get('r')
        return Js(0.0)
    PyJsHoisted_bnCompareTo_.func_name = 'bnCompareTo'
    var.put('bnCompareTo', PyJsHoisted_bnCompareTo_)
    @Js
    def PyJsHoisted_nbits_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'x', 'r'])
        var.put('r', Js(1.0))
        if (var.put('t', PyJsBshift(var.get('x'),Js(16.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(16.0), '+')
        if (var.put('t', (var.get('x')>>Js(8.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(8.0), '+')
        if (var.put('t', (var.get('x')>>Js(4.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(4.0), '+')
        if (var.put('t', (var.get('x')>>Js(2.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(2.0), '+')
        if (var.put('t', (var.get('x')>>Js(1.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(1.0), '+')
        return var.get('r')
    PyJsHoisted_nbits_.func_name = 'nbits'
    var.put('nbits', PyJsHoisted_nbits_)
    @Js
    def PyJsHoisted_bnBitLength_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if (var.get(u"this").get('t')<=Js(0.0)):
            return Js(0.0)
        return ((var.get(u"this").get('DB')*(var.get(u"this").get('t')-Js(1.0)))+var.get('nbits')((var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))^(var.get(u"this").get('s')&var.get(u"this").get('DM')))))
    PyJsHoisted_bnBitLength_.func_name = 'bnBitLength'
    var.put('bnBitLength', PyJsHoisted_bnBitLength_)
    @Js
    def PyJsHoisted_bnpDLShiftTo_(n, r, this, arguments, var=var):
        var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'i', 'r'])
        pass
        #for JS loop
        var.put('i', (var.get(u"this").get('t')-Js(1.0)))
        while (var.get('i')>=Js(0.0)):
            try:
                var.get('r').put((var.get('i')+var.get('n')), var.get(u"this").get(var.get('i')))
            finally:
                    var.put('i',Js(var.get('i').to_number())-Js(1))
        #for JS loop
        var.put('i', (var.get('n')-Js(1.0)))
        while (var.get('i')>=Js(0.0)):
            try:
                var.get('r').put(var.get('i'), Js(0.0))
            finally:
                    var.put('i',Js(var.get('i').to_number())-Js(1))
        var.get('r').put('t', (var.get(u"this").get('t')+var.get('n')))
        var.get('r').put('s', var.get(u"this").get('s'))
    PyJsHoisted_bnpDLShiftTo_.func_name = 'bnpDLShiftTo'
    var.put('bnpDLShiftTo', PyJsHoisted_bnpDLShiftTo_)
    @Js
    def PyJsHoisted_bnpDRShiftTo_(n, r, this, arguments, var=var):
        var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'i', 'r'])
        #for JS loop
        var.put('i', var.get('n'))
        while (var.get('i')<var.get(u"this").get('t')):
            try:
                var.get('r').put((var.get('i')-var.get('n')), var.get(u"this").get(var.get('i')))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        var.get('r').put('t', var.get('Math').callprop('max', (var.get(u"this").get('t')-var.get('n')), Js(0.0)))
        var.get('r').put('s', var.get(u"this").get('s'))
    PyJsHoisted_bnpDRShiftTo_.func_name = 'bnpDRShiftTo'
    var.put('bnpDRShiftTo', PyJsHoisted_bnpDRShiftTo_)
    @Js
    def PyJsHoisted_bnpLShiftTo_(n, r, this, arguments, var=var):
        var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'cbs', 'r', 'bs', 'bm', 'i', 'ds', 'c'])
        var.put('bs', (var.get('n')%var.get(u"this").get('DB')))
        var.put('cbs', (var.get(u"this").get('DB')-var.get('bs')))
        var.put('bm', ((Js(1.0)<<var.get('cbs'))-Js(1.0)))
        var.put('ds', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
        var.put('c', ((var.get(u"this").get('s')<<var.get('bs'))&var.get(u"this").get('DM')))
        #for JS loop
        var.put('i', (var.get(u"this").get('t')-Js(1.0)))
        while (var.get('i')>=Js(0.0)):
            try:
                var.get('r').put(((var.get('i')+var.get('ds'))+Js(1.0)), ((var.get(u"this").get(var.get('i'))>>var.get('cbs'))|var.get('c')))
                var.put('c', ((var.get(u"this").get(var.get('i'))&var.get('bm'))<<var.get('bs')))
            finally:
                    var.put('i',Js(var.get('i').to_number())-Js(1))
        #for JS loop
        var.put('i', (var.get('ds')-Js(1.0)))
        while (var.get('i')>=Js(0.0)):
            try:
                var.get('r').put(var.get('i'), Js(0.0))
            finally:
                    var.put('i',Js(var.get('i').to_number())-Js(1))
        var.get('r').put(var.get('ds'), var.get('c'))
        var.get('r').put('t', ((var.get(u"this").get('t')+var.get('ds'))+Js(1.0)))
        var.get('r').put('s', var.get(u"this").get('s'))
        var.get('r').callprop('clamp')
    PyJsHoisted_bnpLShiftTo_.func_name = 'bnpLShiftTo'
    var.put('bnpLShiftTo', PyJsHoisted_bnpLShiftTo_)
    @Js
    def PyJsHoisted_bnpRShiftTo_(n, r, this, arguments, var=var):
        var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'cbs', 'r', 'bs', 'bm', 'i', 'ds'])
        var.get('r').put('s', var.get(u"this").get('s'))
        var.put('ds', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
        if (var.get('ds')>=var.get(u"this").get('t')):
            var.get('r').put('t', Js(0.0))
            return var.get('undefined')
        var.put('bs', (var.get('n')%var.get(u"this").get('DB')))
        var.put('cbs', (var.get(u"this").get('DB')-var.get('bs')))
        var.put('bm', ((Js(1.0)<<var.get('bs'))-Js(1.0)))
        var.get('r').put('0', (var.get(u"this").get(var.get('ds'))>>var.get('bs')))
        #for JS loop
        var.put('i', (var.get('ds')+Js(1.0)))
        while (var.get('i')<var.get(u"this").get('t')):
            try:
                var.get('r').put(((var.get('i')-var.get('ds'))-Js(1.0)), ((var.get(u"this").get(var.get('i'))&var.get('bm'))<<var.get('cbs')), '|')
                var.get('r').put((var.get('i')-var.get('ds')), (var.get(u"this").get(var.get('i'))>>var.get('bs')))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        if (var.get('bs')>Js(0.0)):
            var.get('r').put(((var.get(u"this").get('t')-var.get('ds'))-Js(1.0)), ((var.get(u"this").get('s')&var.get('bm'))<<var.get('cbs')), '|')
        var.get('r').put('t', (var.get(u"this").get('t')-var.get('ds')))
        var.get('r').callprop('clamp')
    PyJsHoisted_bnpRShiftTo_.func_name = 'bnpRShiftTo'
    var.put('bnpRShiftTo', PyJsHoisted_bnpRShiftTo_)
    @Js
    def PyJsHoisted_bnpSubTo_(a, r, this, arguments, var=var):
        var = Scope({'a':a, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'i', 'a', 'm', 'c'])
        var.put('i', Js(0.0))
        var.put('c', Js(0.0))
        var.put('m', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
        while (var.get('i')<var.get('m')):
            var.put('c', (var.get(u"this").get(var.get('i'))-var.get('a').get(var.get('i'))), '+')
            var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
            var.put('c', var.get(u"this").get('DB'), '>>')
        if (var.get('a').get('t')<var.get(u"this").get('t')):
            var.put('c', var.get('a').get('s'), '-')
            while (var.get('i')<var.get(u"this").get('t')):
                var.put('c', var.get(u"this").get(var.get('i')), '+')
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                var.put('c', var.get(u"this").get('DB'), '>>')
            var.put('c', var.get(u"this").get('s'), '+')
        else:
            var.put('c', var.get(u"this").get('s'), '+')
            while (var.get('i')<var.get('a').get('t')):
                var.put('c', var.get('a').get(var.get('i')), '-')
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                var.put('c', var.get(u"this").get('DB'), '>>')
            var.put('c', var.get('a').get('s'), '-')
        var.get('r').put('s', ((-Js(1.0)) if (var.get('c')<Js(0.0)) else Js(0.0)))
        if (var.get('c')<(-Js(1.0))):
            var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get(u"this").get('DV')+var.get('c')))
        else:
            if (var.get('c')>Js(0.0)):
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), var.get('c'))
        var.get('r').put('t', var.get('i'))
        var.get('r').callprop('clamp')
    PyJsHoisted_bnpSubTo_.func_name = 'bnpSubTo'
    var.put('bnpSubTo', PyJsHoisted_bnpSubTo_)
    @Js
    def PyJsHoisted_bnpMultiplyTo_(a, r, this, arguments, var=var):
        var = Scope({'a':a, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'i', 'a', 'y', 'x'])
        var.put('x', var.get(u"this").callprop('abs'))
        var.put('y', var.get('a').callprop('abs'))
        var.put('i', var.get('x').get('t'))
        var.get('r').put('t', (var.get('i')+var.get('y').get('t')))
        while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
            var.get('r').put(var.get('i'), Js(0.0))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('y').get('t')):
            try:
                var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').callprop('am', Js(0.0), var.get('y').get(var.get('i')), var.get('r'), var.get('i'), Js(0.0), var.get('x').get('t')))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        var.get('r').put('s', Js(0.0))
        var.get('r').callprop('clamp')
        if (var.get(u"this").get('s')!=var.get('a').get('s')):
            var.get('BigInteger').get('ZERO').callprop('subTo', var.get('r'), var.get('r'))
    PyJsHoisted_bnpMultiplyTo_.func_name = 'bnpMultiplyTo'
    var.put('bnpMultiplyTo', PyJsHoisted_bnpMultiplyTo_)
    @Js
    def PyJsHoisted_bnpSquareTo_(r, this, arguments, var=var):
        var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'c', 'x', 'r'])
        var.put('x', var.get(u"this").callprop('abs'))
        var.put('i', var.get('r').put('t', (Js(2.0)*var.get('x').get('t'))))
        while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
            var.get('r').put(var.get('i'), Js(0.0))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<(var.get('x').get('t')-Js(1.0))):
            try:
                var.put('c', var.get('x').callprop('am', var.get('i'), var.get('x').get(var.get('i')), var.get('r'), (Js(2.0)*var.get('i')), Js(0.0), Js(1.0)))
                if (var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').callprop('am', (var.get('i')+Js(1.0)), (Js(2.0)*var.get('x').get(var.get('i'))), var.get('r'), ((Js(2.0)*var.get('i'))+Js(1.0)), var.get('c'), ((var.get('x').get('t')-var.get('i'))-Js(1.0))), '+')>=var.get('x').get('DV')):
                    var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').get('DV'), '-')
                    var.get('r').put(((var.get('i')+var.get('x').get('t'))+Js(1.0)), Js(1.0))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        if (var.get('r').get('t')>Js(0.0)):
            var.get('r').put((var.get('r').get('t')-Js(1.0)), var.get('x').callprop('am', var.get('i'), var.get('x').get(var.get('i')), var.get('r'), (Js(2.0)*var.get('i')), Js(0.0), Js(1.0)), '+')
        var.get('r').put('s', Js(0.0))
        var.get('r').callprop('clamp')
    PyJsHoisted_bnpSquareTo_.func_name = 'bnpSquareTo'
    var.put('bnpSquareTo', PyJsHoisted_bnpSquareTo_)
    @Js
    def PyJsHoisted_bnpDivRemTo_(m, q, r, this, arguments, var=var):
        var = Scope({'m':m, 'q':q, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['nsh', 'd1', 'r', 'qd', 'ts', 'q', 'm', 'pt', 'j', 'i', 'y', 'd2', 'yt', 'pm', 'ms', 'e', 't', 'ys', 'y0'])
        var.put('pm', var.get('m').callprop('abs'))
        if (var.get('pm').get('t')<=Js(0.0)):
            return var.get('undefined')
        var.put('pt', var.get(u"this").callprop('abs'))
        if (var.get('pt').get('t')<var.get('pm').get('t')):
            if (var.get('q')!=var.get(u"null")):
                var.get('q').callprop('fromInt', Js(0.0))
            if (var.get('r')!=var.get(u"null")):
                var.get(u"this").callprop('copyTo', var.get('r'))
            return var.get('undefined')
        if (var.get('r')==var.get(u"null")):
            var.put('r', var.get('nbi')())
        var.put('y', var.get('nbi')())
        var.put('ts', var.get(u"this").get('s'))
        var.put('ms', var.get('m').get('s'))
        var.put('nsh', (var.get(u"this").get('DB')-var.get('nbits')(var.get('pm').get((var.get('pm').get('t')-Js(1.0))))))
        if (var.get('nsh')>Js(0.0)):
            var.get('pm').callprop('lShiftTo', var.get('nsh'), var.get('y'))
            var.get('pt').callprop('lShiftTo', var.get('nsh'), var.get('r'))
        else:
            var.get('pm').callprop('copyTo', var.get('y'))
            var.get('pt').callprop('copyTo', var.get('r'))
        var.put('ys', var.get('y').get('t'))
        var.put('y0', var.get('y').get((var.get('ys')-Js(1.0))))
        if (var.get('y0')==Js(0.0)):
            return var.get('undefined')
        var.put('yt', ((var.get('y0')*(Js(1.0)<<var.get(u"this").get('F1')))+((var.get('y').get((var.get('ys')-Js(2.0)))>>var.get(u"this").get('F2')) if (var.get('ys')>Js(1.0)) else Js(0.0))))
        var.put('d1', (var.get(u"this").get('FV')/var.get('yt')))
        var.put('d2', ((Js(1.0)<<var.get(u"this").get('F1'))/var.get('yt')))
        var.put('e', (Js(1.0)<<var.get(u"this").get('F2')))
        var.put('i', var.get('r').get('t'))
        var.put('j', (var.get('i')-var.get('ys')))
        var.put('t', (var.get('nbi')() if (var.get('q')==var.get(u"null")) else var.get('q')))
        var.get('y').callprop('dlShiftTo', var.get('j'), var.get('t'))
        if (var.get('r').callprop('compareTo', var.get('t'))>=Js(0.0)):
            var.get('r').put((var.get('r').put('t',Js(var.get('r').get('t').to_number())+Js(1))-Js(1)), Js(1.0))
            var.get('r').callprop('subTo', var.get('t'), var.get('r'))
        var.get('BigInteger').get('ONE').callprop('dlShiftTo', var.get('ys'), var.get('t'))
        var.get('t').callprop('subTo', var.get('y'), var.get('y'))
        while (var.get('y').get('t')<var.get('ys')):
            var.get('y').put((var.get('y').put('t',Js(var.get('y').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
        while (var.put('j',Js(var.get('j').to_number())-Js(1))>=Js(0.0)):
            var.put('qd', (var.get(u"this").get('DM') if (var.get('r').get(var.put('i',Js(var.get('i').to_number())-Js(1)))==var.get('y0')) else var.get('Math').callprop('floor', ((var.get('r').get(var.get('i'))*var.get('d1'))+((var.get('r').get((var.get('i')-Js(1.0)))+var.get('e'))*var.get('d2'))))))
            if (var.get('r').put(var.get('i'), var.get('y').callprop('am', Js(0.0), var.get('qd'), var.get('r'), var.get('j'), Js(0.0), var.get('ys')), '+')<var.get('qd')):
                var.get('y').callprop('dlShiftTo', var.get('j'), var.get('t'))
                var.get('r').callprop('subTo', var.get('t'), var.get('r'))
                while (var.get('r').get(var.get('i'))<var.put('qd',Js(var.get('qd').to_number())-Js(1))):
                    var.get('r').callprop('subTo', var.get('t'), var.get('r'))
        if (var.get('q')!=var.get(u"null")):
            var.get('r').callprop('drShiftTo', var.get('ys'), var.get('q'))
            if (var.get('ts')!=var.get('ms')):
                var.get('BigInteger').get('ZERO').callprop('subTo', var.get('q'), var.get('q'))
        var.get('r').put('t', var.get('ys'))
        var.get('r').callprop('clamp')
        if (var.get('nsh')>Js(0.0)):
            var.get('r').callprop('rShiftTo', var.get('nsh'), var.get('r'))
        if (var.get('ts')<Js(0.0)):
            var.get('BigInteger').get('ZERO').callprop('subTo', var.get('r'), var.get('r'))
    PyJsHoisted_bnpDivRemTo_.func_name = 'bnpDivRemTo'
    var.put('bnpDivRemTo', PyJsHoisted_bnpDivRemTo_)
    @Js
    def PyJsHoisted_bnMod_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('abs').callprop('divRemTo', var.get('a'), var.get(u"null"), var.get('r'))
        if ((var.get(u"this").get('s')<Js(0.0)) and (var.get('r').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))):
            var.get('a').callprop('subTo', var.get('r'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnMod_.func_name = 'bnMod'
    var.put('bnMod', PyJsHoisted_bnMod_)
    @Js
    def PyJsHoisted_Classic_(m, this, arguments, var=var):
        var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
        var.registers(['m'])
        var.get(u"this").put('m', var.get('m'))
    PyJsHoisted_Classic_.func_name = 'Classic'
    var.put('Classic', PyJsHoisted_Classic_)
    @Js
    def PyJsHoisted_cConvert_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x'])
        if ((var.get('x').get('s')<Js(0.0)) or (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0))):
            return var.get('x').callprop('mod', var.get(u"this").get('m'))
        else:
            return var.get('x')
    PyJsHoisted_cConvert_.func_name = 'cConvert'
    var.put('cConvert', PyJsHoisted_cConvert_)
    @Js
    def PyJsHoisted_cRevert_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x'])
        return var.get('x')
    PyJsHoisted_cRevert_.func_name = 'cRevert'
    var.put('cRevert', PyJsHoisted_cRevert_)
    @Js
    def PyJsHoisted_cReduce_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x'])
        var.get('x').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('x'))
    PyJsHoisted_cReduce_.func_name = 'cReduce'
    var.put('cReduce', PyJsHoisted_cReduce_)
    @Js
    def PyJsHoisted_cMulTo_(x, y, r, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x', 'r'])
        var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
        var.get(u"this").callprop('reduce', var.get('r'))
    PyJsHoisted_cMulTo_.func_name = 'cMulTo'
    var.put('cMulTo', PyJsHoisted_cMulTo_)
    @Js
    def PyJsHoisted_cSqrTo_(x, r, this, arguments, var=var):
        var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        var.get('x').callprop('squareTo', var.get('r'))
        var.get(u"this").callprop('reduce', var.get('r'))
    PyJsHoisted_cSqrTo_.func_name = 'cSqrTo'
    var.put('cSqrTo', PyJsHoisted_cSqrTo_)
    @Js
    def PyJsHoisted_bnpInvDigit_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        if (var.get(u"this").get('t')<Js(1.0)):
            return Js(0.0)
        var.put('x', var.get(u"this").get('0'))
        if ((var.get('x')&Js(1.0))==Js(0.0)):
            return Js(0.0)
        var.put('y', (var.get('x')&Js(3.0)))
        var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')&Js(15))*var.get('y'))))&Js(15)))
        var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')&Js(255))*var.get('y'))))&Js(255)))
        var.put('y', ((var.get('y')*(Js(2.0)-(((var.get('x')&Js(65535))*var.get('y'))&Js(65535))))&Js(65535)))
        var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')*var.get('y'))%var.get(u"this").get('DV'))))%var.get(u"this").get('DV')))
        return ((var.get(u"this").get('DV')-var.get('y')) if (var.get('y')>Js(0.0)) else (-var.get('y')))
    PyJsHoisted_bnpInvDigit_.func_name = 'bnpInvDigit'
    var.put('bnpInvDigit', PyJsHoisted_bnpInvDigit_)
    @Js
    def PyJsHoisted_Montgomery_(m, this, arguments, var=var):
        var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
        var.registers(['m'])
        var.get(u"this").put('m', var.get('m'))
        var.get(u"this").put('mp', var.get('m').callprop('invDigit'))
        var.get(u"this").put('mpl', (var.get(u"this").get('mp')&Js(32767)))
        var.get(u"this").put('mph', (var.get(u"this").get('mp')>>Js(15.0)))
        var.get(u"this").put('um', ((Js(1.0)<<(var.get('m').get('DB')-Js(15.0)))-Js(1.0)))
        var.get(u"this").put('mt2', (Js(2.0)*var.get('m').get('t')))
    PyJsHoisted_Montgomery_.func_name = 'Montgomery'
    var.put('Montgomery', PyJsHoisted_Montgomery_)
    @Js
    def PyJsHoisted_montConvert_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        var.put('r', var.get('nbi')())
        var.get('x').callprop('abs').callprop('dlShiftTo', var.get(u"this").get('m').get('t'), var.get('r'))
        var.get('r').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('r'))
        if ((var.get('x').get('s')<Js(0.0)) and (var.get('r').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))):
            var.get(u"this").get('m').callprop('subTo', var.get('r'), var.get('r'))
        return var.get('r')
    PyJsHoisted_montConvert_.func_name = 'montConvert'
    var.put('montConvert', PyJsHoisted_montConvert_)
    @Js
    def PyJsHoisted_montRevert_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        var.put('r', var.get('nbi')())
        var.get('x').callprop('copyTo', var.get('r'))
        var.get(u"this").callprop('reduce', var.get('r'))
        return var.get('r')
    PyJsHoisted_montRevert_.func_name = 'montRevert'
    var.put('montRevert', PyJsHoisted_montRevert_)
    @Js
    def PyJsHoisted_montReduce_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['u0', 'j', 'x', 'i'])
        while (var.get('x').get('t')<=var.get(u"this").get('mt2')):
            var.get('x').put((var.get('x').put('t',Js(var.get('x').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get(u"this").get('m').get('t')):
            try:
                var.put('j', (var.get('x').get(var.get('i'))&Js(32767)))
                var.put('u0', (((var.get('j')*var.get(u"this").get('mpl'))+((((var.get('j')*var.get(u"this").get('mph'))+((var.get('x').get(var.get('i'))>>Js(15.0))*var.get(u"this").get('mpl')))&var.get(u"this").get('um'))<<Js(15.0)))&var.get('x').get('DM')))
                var.put('j', (var.get('i')+var.get(u"this").get('m').get('t')))
                var.get('x').put(var.get('j'), var.get(u"this").get('m').callprop('am', Js(0.0), var.get('u0'), var.get('x'), var.get('i'), Js(0.0), var.get(u"this").get('m').get('t')), '+')
                while (var.get('x').get(var.get('j'))>=var.get('x').get('DV')):
                    var.get('x').put(var.get('j'), var.get('x').get('DV'), '-')
                    (var.get('x').put(var.put('j',Js(var.get('j').to_number())+Js(1)),Js(var.get('x').get(var.put('j',Js(var.get('j').to_number())+Js(1))).to_number())+Js(1))-Js(1))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        var.get('x').callprop('clamp')
        var.get('x').callprop('drShiftTo', var.get(u"this").get('m').get('t'), var.get('x'))
        if (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0)):
            var.get('x').callprop('subTo', var.get(u"this").get('m'), var.get('x'))
    PyJsHoisted_montReduce_.func_name = 'montReduce'
    var.put('montReduce', PyJsHoisted_montReduce_)
    @Js
    def PyJsHoisted_montSqrTo_(x, r, this, arguments, var=var):
        var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        var.get('x').callprop('squareTo', var.get('r'))
        var.get(u"this").callprop('reduce', var.get('r'))
    PyJsHoisted_montSqrTo_.func_name = 'montSqrTo'
    var.put('montSqrTo', PyJsHoisted_montSqrTo_)
    @Js
    def PyJsHoisted_montMulTo_(x, y, r, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x', 'r'])
        var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
        var.get(u"this").callprop('reduce', var.get('r'))
    PyJsHoisted_montMulTo_.func_name = 'montMulTo'
    var.put('montMulTo', PyJsHoisted_montMulTo_)
    @Js
    def PyJsHoisted_bnpIsEven_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (((var.get(u"this").get('0')&Js(1.0)) if (var.get(u"this").get('t')>Js(0.0)) else var.get(u"this").get('s'))==Js(0.0))
    PyJsHoisted_bnpIsEven_.func_name = 'bnpIsEven'
    var.put('bnpIsEven', PyJsHoisted_bnpIsEven_)
    @Js
    def PyJsHoisted_bnpExp_(e, z, this, arguments, var=var):
        var = Scope({'e':e, 'z':z, 'this':this, 'arguments':arguments}, var)
        var.registers(['r2', 'r', 'e', 't', 'z', 'i', 'g'])
        if ((var.get('e')>Js(4294967295)) or (var.get('e')<Js(1.0))):
            return var.get('BigInteger').get('ONE')
        var.put('r', var.get('nbi')())
        var.put('r2', var.get('nbi')())
        var.put('g', var.get('z').callprop('convert', var.get(u"this")))
        var.put('i', (var.get('nbits')(var.get('e'))-Js(1.0)))
        var.get('g').callprop('copyTo', var.get('r'))
        while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
            var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
            if ((var.get('e')&(Js(1.0)<<var.get('i')))>Js(0.0)):
                var.get('z').callprop('mulTo', var.get('r2'), var.get('g'), var.get('r'))
            else:
                var.put('t', var.get('r'))
                var.put('r', var.get('r2'))
                var.put('r2', var.get('t'))
        return var.get('z').callprop('revert', var.get('r'))
    PyJsHoisted_bnpExp_.func_name = 'bnpExp'
    var.put('bnpExp', PyJsHoisted_bnpExp_)
    @Js
    def PyJsHoisted_bnModPowInt_(e, m, this, arguments, var=var):
        var = Scope({'e':e, 'm':m, 'this':this, 'arguments':arguments}, var)
        var.registers(['m', 'z', 'e'])
        pass
        if ((var.get('e')<Js(256.0)) or var.get('m').callprop('isEven')):
            var.put('z', var.get('Classic').create(var.get('m')))
        else:
            var.put('z', var.get('Montgomery').create(var.get('m')))
        return var.get(u"this").callprop('exp', var.get('e'), var.get('z'))
    PyJsHoisted_bnModPowInt_.func_name = 'bnModPowInt'
    var.put('bnModPowInt', PyJsHoisted_bnModPowInt_)
    @Js
    def PyJsHoisted_bnClone_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('copyTo', var.get('r'))
        return var.get('r')
    PyJsHoisted_bnClone_.func_name = 'bnClone'
    var.put('bnClone', PyJsHoisted_bnClone_)
    @Js
    def PyJsHoisted_bnIntValue_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if (var.get(u"this").get('s')<Js(0.0)):
            if (var.get(u"this").get('t')==Js(1.0)):
                return (var.get(u"this").get('0')-var.get(u"this").get('DV'))
            else:
                if (var.get(u"this").get('t')==Js(0.0)):
                    return (-Js(1.0))
        else:
            if (var.get(u"this").get('t')==Js(1.0)):
                return var.get(u"this").get('0')
            else:
                if (var.get(u"this").get('t')==Js(0.0)):
                    return Js(0.0)
        return (((var.get(u"this").get('1')&((Js(1.0)<<(Js(32.0)-var.get(u"this").get('DB')))-Js(1.0)))<<var.get(u"this").get('DB'))|var.get(u"this").get('0'))
    PyJsHoisted_bnIntValue_.func_name = 'bnIntValue'
    var.put('bnIntValue', PyJsHoisted_bnIntValue_)
    @Js
    def PyJsHoisted_bnByteValue_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (var.get(u"this").get('s') if (var.get(u"this").get('t')==Js(0.0)) else ((var.get(u"this").get('0')<<Js(24.0))>>Js(24.0)))
    PyJsHoisted_bnByteValue_.func_name = 'bnByteValue'
    var.put('bnByteValue', PyJsHoisted_bnByteValue_)
    @Js
    def PyJsHoisted_bnShortValue_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (var.get(u"this").get('s') if (var.get(u"this").get('t')==Js(0.0)) else ((var.get(u"this").get('0')<<Js(16.0))>>Js(16.0)))
    PyJsHoisted_bnShortValue_.func_name = 'bnShortValue'
    var.put('bnShortValue', PyJsHoisted_bnShortValue_)
    @Js
    def PyJsHoisted_bnpChunkSize_(r, this, arguments, var=var):
        var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r'])
        return var.get('Math').callprop('floor', ((var.get('Math').get('LN2')*var.get(u"this").get('DB'))/var.get('Math').callprop('log', var.get('r'))))
    PyJsHoisted_bnpChunkSize_.func_name = 'bnpChunkSize'
    var.put('bnpChunkSize', PyJsHoisted_bnpChunkSize_)
    @Js
    def PyJsHoisted_bnSigNum_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        if (var.get(u"this").get('s')<Js(0.0)):
            return (-Js(1.0))
        else:
            if ((var.get(u"this").get('t')<=Js(0.0)) or ((var.get(u"this").get('t')==Js(1.0)) and (var.get(u"this").get('0')<=Js(0.0)))):
                return Js(0.0)
            else:
                return Js(1.0)
    PyJsHoisted_bnSigNum_.func_name = 'bnSigNum'
    var.put('bnSigNum', PyJsHoisted_bnSigNum_)
    @Js
    def PyJsHoisted_bnpToRadix_(b, this, arguments, var=var):
        var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['d', 'b', 'cs', 'r', 'z', 'a', 'y'])
        if (var.get('b')==var.get(u"null")):
            var.put('b', Js(10.0))
        if (((var.get(u"this").callprop('signum')==Js(0.0)) or (var.get('b')<Js(2.0))) or (var.get('b')>Js(36.0))):
            return Js('0')
        var.put('cs', var.get(u"this").callprop('chunkSize', var.get('b')))
        var.put('a', var.get('Math').callprop('pow', var.get('b'), var.get('cs')))
        var.put('d', var.get('nbv')(var.get('a')))
        var.put('y', var.get('nbi')())
        var.put('z', var.get('nbi')())
        var.put('r', Js(''))
        var.get(u"this").callprop('divRemTo', var.get('d'), var.get('y'), var.get('z'))
        while (var.get('y').callprop('signum')>Js(0.0)):
            var.put('r', ((var.get('a')+var.get('z').callprop('intValue')).callprop('toString', var.get('b')).callprop('substr', Js(1.0))+var.get('r')))
            var.get('y').callprop('divRemTo', var.get('d'), var.get('y'), var.get('z'))
        return (var.get('z').callprop('intValue').callprop('toString', var.get('b'))+var.get('r'))
    PyJsHoisted_bnpToRadix_.func_name = 'bnpToRadix'
    var.put('bnpToRadix', PyJsHoisted_bnpToRadix_)
    @Js
    def PyJsHoisted_bnpFromRadix_(s, b, this, arguments, var=var):
        var = Scope({'s':s, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['j', 'd', 's', 'cs', 'b', 'w', 'i', 'mi', 'x'])
        var.get(u"this").callprop('fromInt', Js(0.0))
        if (var.get('b')==var.get(u"null")):
            var.put('b', Js(10.0))
        var.put('cs', var.get(u"this").callprop('chunkSize', var.get('b')))
        var.put('d', var.get('Math').callprop('pow', var.get('b'), var.get('cs')))
        var.put('mi', Js(False))
        var.put('j', Js(0.0))
        var.put('w', Js(0.0))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('s').get('length')):
            try:
                var.put('x', var.get('intAt')(var.get('s'), var.get('i')))
                if (var.get('x')<Js(0.0)):
                    if ((var.get('s').callprop('charAt', var.get('i'))==Js('-')) and (var.get(u"this").callprop('signum')==Js(0.0))):
                        var.put('mi', Js(True))
                    continue
                var.put('w', ((var.get('b')*var.get('w'))+var.get('x')))
                if (var.put('j',Js(var.get('j').to_number())+Js(1))>=var.get('cs')):
                    var.get(u"this").callprop('dMultiply', var.get('d'))
                    var.get(u"this").callprop('dAddOffset', var.get('w'), Js(0.0))
                    var.put('j', Js(0.0))
                    var.put('w', Js(0.0))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        if (var.get('j')>Js(0.0)):
            var.get(u"this").callprop('dMultiply', var.get('Math').callprop('pow', var.get('b'), var.get('j')))
            var.get(u"this").callprop('dAddOffset', var.get('w'), Js(0.0))
        if var.get('mi'):
            var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get(u"this"))
    PyJsHoisted_bnpFromRadix_.func_name = 'bnpFromRadix'
    var.put('bnpFromRadix', PyJsHoisted_bnpFromRadix_)
    @Js
    def PyJsHoisted_bnpFromNumber_(a, b, c, this, arguments, var=var):
        var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
        var.registers(['b', 't', 'a', 'c', 'x'])
        if (Js('number')==var.get('b',throw=False).typeof()):
            if (var.get('a')<Js(2.0)):
                var.get(u"this").callprop('fromInt', Js(1.0))
            else:
                var.get(u"this").callprop('fromNumber', var.get('a'), var.get('c'))
                if var.get(u"this").callprop('testBit', (var.get('a')-Js(1.0))).neg():
                    var.get(u"this").callprop('bitwiseTo', var.get('BigInteger').get('ONE').callprop('shiftLeft', (var.get('a')-Js(1.0))), var.get('op_or'), var.get(u"this"))
                if var.get(u"this").callprop('isEven'):
                    var.get(u"this").callprop('dAddOffset', Js(1.0), Js(0.0))
                while var.get(u"this").callprop('isProbablePrime', var.get('b')).neg():
                    var.get(u"this").callprop('dAddOffset', Js(2.0), Js(0.0))
                    if (var.get(u"this").callprop('bitLength')>var.get('a')):
                        var.get(u"this").callprop('subTo', var.get('BigInteger').get('ONE').callprop('shiftLeft', (var.get('a')-Js(1.0))), var.get(u"this"))
        else:
            var.put('x', var.get('Array').create())
            var.put('t', (var.get('a')&Js(7.0)))
            var.get('x').put('length', ((var.get('a')>>Js(3.0))+Js(1.0)))
            var.get('b').callprop('nextBytes', var.get('x'))
            if (var.get('t')>Js(0.0)):
                var.get('x').put('0', ((Js(1.0)<<var.get('t'))-Js(1.0)), '&')
            else:
                var.get('x').put('0', Js(0.0))
            var.get(u"this").callprop('fromString', var.get('x'), Js(256.0))
    PyJsHoisted_bnpFromNumber_.func_name = 'bnpFromNumber'
    var.put('bnpFromNumber', PyJsHoisted_bnpFromNumber_)
    @Js
    def PyJsHoisted_bnToByteArray_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['k', 'd', 'p', 'r', 'i'])
        var.put('i', var.get(u"this").get('t'))
        var.put('r', var.get('Array').create())
        var.get('r').put('0', var.get(u"this").get('s'))
        var.put('p', (var.get(u"this").get('DB')-((var.get('i')*var.get(u"this").get('DB'))%Js(8.0))))
        var.put('k', Js(0.0))
        if ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
            if ((var.get('p')<var.get(u"this").get('DB')) and (var.put('d', (var.get(u"this").get(var.get('i'))>>var.get('p')))!=((var.get(u"this").get('s')&var.get(u"this").get('DM'))>>var.get('p')))):
                var.get('r').put((var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1)), (var.get('d')|(var.get(u"this").get('s')<<(var.get(u"this").get('DB')-var.get('p')))))
            while (var.get('i')>=Js(0.0)):
                if (var.get('p')<Js(8.0)):
                    var.put('d', ((var.get(u"this").get(var.get('i'))&((Js(1.0)<<var.get('p'))-Js(1.0)))<<(Js(8.0)-var.get('p'))))
                    var.put('d', (var.get(u"this").get(var.put('i',Js(var.get('i').to_number())-Js(1)))>>var.put('p', (var.get(u"this").get('DB')-Js(8.0)), '+')), '|')
                else:
                    var.put('d', ((var.get(u"this").get(var.get('i'))>>var.put('p', Js(8.0), '-'))&Js(255)))
                    if (var.get('p')<=Js(0.0)):
                        var.put('p', var.get(u"this").get('DB'), '+')
                        var.put('i',Js(var.get('i').to_number())-Js(1))
                if ((var.get('d')&Js(128))!=Js(0.0)):
                    var.put('d', (-Js(256.0)), '|')
                if ((var.get('k')==Js(0.0)) and ((var.get(u"this").get('s')&Js(128))!=(var.get('d')&Js(128)))):
                    var.put('k',Js(var.get('k').to_number())+Js(1))
                if ((var.get('k')>Js(0.0)) or (var.get('d')!=var.get(u"this").get('s'))):
                    var.get('r').put((var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1)), var.get('d'))
        return var.get('r')
    PyJsHoisted_bnToByteArray_.func_name = 'bnToByteArray'
    var.put('bnToByteArray', PyJsHoisted_bnToByteArray_)
    @Js
    def PyJsHoisted_bnEquals_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a'])
        return (var.get(u"this").callprop('compareTo', var.get('a'))==Js(0.0))
    PyJsHoisted_bnEquals_.func_name = 'bnEquals'
    var.put('bnEquals', PyJsHoisted_bnEquals_)
    @Js
    def PyJsHoisted_bnMin_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a'])
        return (var.get(u"this") if (var.get(u"this").callprop('compareTo', var.get('a'))<Js(0.0)) else var.get('a'))
    PyJsHoisted_bnMin_.func_name = 'bnMin'
    var.put('bnMin', PyJsHoisted_bnMin_)
    @Js
    def PyJsHoisted_bnMax_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a'])
        return (var.get(u"this") if (var.get(u"this").callprop('compareTo', var.get('a'))>Js(0.0)) else var.get('a'))
    PyJsHoisted_bnMax_.func_name = 'bnMax'
    var.put('bnMax', PyJsHoisted_bnMax_)
    @Js
    def PyJsHoisted_bnpBitwiseTo_(a, op, r, this, arguments, var=var):
        var = Scope({'a':a, 'op':op, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['op', 'f', 'r', 'i', 'a', 'm'])
        var.put('m', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('m')):
            try:
                var.get('r').put(var.get('i'), var.get('op')(var.get(u"this").get(var.get('i')), var.get('a').get(var.get('i'))))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        if (var.get('a').get('t')<var.get(u"this").get('t')):
            var.put('f', (var.get('a').get('s')&var.get(u"this").get('DM')))
            #for JS loop
            var.put('i', var.get('m'))
            while (var.get('i')<var.get(u"this").get('t')):
                try:
                    var.get('r').put(var.get('i'), var.get('op')(var.get(u"this").get(var.get('i')), var.get('f')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').put('t', var.get(u"this").get('t'))
        else:
            var.put('f', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
            #for JS loop
            var.put('i', var.get('m'))
            while (var.get('i')<var.get('a').get('t')):
                try:
                    var.get('r').put(var.get('i'), var.get('op')(var.get('f'), var.get('a').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').put('t', var.get('a').get('t'))
        var.get('r').put('s', var.get('op')(var.get(u"this").get('s'), var.get('a').get('s')))
        var.get('r').callprop('clamp')
    PyJsHoisted_bnpBitwiseTo_.func_name = 'bnpBitwiseTo'
    var.put('bnpBitwiseTo', PyJsHoisted_bnpBitwiseTo_)
    @Js
    def PyJsHoisted_op_and_(x, y, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        return (var.get('x')&var.get('y'))
    PyJsHoisted_op_and_.func_name = 'op_and'
    var.put('op_and', PyJsHoisted_op_and_)
    @Js
    def PyJsHoisted_bnAnd_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('bitwiseTo', var.get('a'), var.get('op_and'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnAnd_.func_name = 'bnAnd'
    var.put('bnAnd', PyJsHoisted_bnAnd_)
    @Js
    def PyJsHoisted_op_or_(x, y, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        return (var.get('x')|var.get('y'))
    PyJsHoisted_op_or_.func_name = 'op_or'
    var.put('op_or', PyJsHoisted_op_or_)
    @Js
    def PyJsHoisted_bnOr_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('bitwiseTo', var.get('a'), var.get('op_or'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnOr_.func_name = 'bnOr'
    var.put('bnOr', PyJsHoisted_bnOr_)
    @Js
    def PyJsHoisted_op_xor_(x, y, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        return (var.get('x')^var.get('y'))
    PyJsHoisted_op_xor_.func_name = 'op_xor'
    var.put('op_xor', PyJsHoisted_op_xor_)
    @Js
    def PyJsHoisted_bnXor_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('bitwiseTo', var.get('a'), var.get('op_xor'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnXor_.func_name = 'bnXor'
    var.put('bnXor', PyJsHoisted_bnXor_)
    @Js
    def PyJsHoisted_op_andnot_(x, y, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        return (var.get('x')&(~var.get('y')))
    PyJsHoisted_op_andnot_.func_name = 'op_andnot'
    var.put('op_andnot', PyJsHoisted_op_andnot_)
    @Js
    def PyJsHoisted_bnAndNot_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('bitwiseTo', var.get('a'), var.get('op_andnot'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnAndNot_.func_name = 'bnAndNot'
    var.put('bnAndNot', PyJsHoisted_bnAndNot_)
    @Js
    def PyJsHoisted_bnNot_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'r'])
        var.put('r', var.get('nbi')())
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get(u"this").get('t')):
            try:
                var.get('r').put(var.get('i'), (var.get(u"this").get('DM')&(~var.get(u"this").get(var.get('i')))))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        var.get('r').put('t', var.get(u"this").get('t'))
        var.get('r').put('s', (~var.get(u"this").get('s')))
        return var.get('r')
    PyJsHoisted_bnNot_.func_name = 'bnNot'
    var.put('bnNot', PyJsHoisted_bnNot_)
    @Js
    def PyJsHoisted_bnShiftLeft_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'r'])
        var.put('r', var.get('nbi')())
        if (var.get('n')<Js(0.0)):
            var.get(u"this").callprop('rShiftTo', (-var.get('n')), var.get('r'))
        else:
            var.get(u"this").callprop('lShiftTo', var.get('n'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnShiftLeft_.func_name = 'bnShiftLeft'
    var.put('bnShiftLeft', PyJsHoisted_bnShiftLeft_)
    @Js
    def PyJsHoisted_bnShiftRight_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'r'])
        var.put('r', var.get('nbi')())
        if (var.get('n')<Js(0.0)):
            var.get(u"this").callprop('lShiftTo', (-var.get('n')), var.get('r'))
        else:
            var.get(u"this").callprop('rShiftTo', var.get('n'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnShiftRight_.func_name = 'bnShiftRight'
    var.put('bnShiftRight', PyJsHoisted_bnShiftRight_)
    @Js
    def PyJsHoisted_lbit_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        if (var.get('x')==Js(0.0)):
            return (-Js(1.0))
        var.put('r', Js(0.0))
        if ((var.get('x')&Js(65535))==Js(0.0)):
            var.put('x', Js(16.0), '>>')
            var.put('r', Js(16.0), '+')
        if ((var.get('x')&Js(255))==Js(0.0)):
            var.put('x', Js(8.0), '>>')
            var.put('r', Js(8.0), '+')
        if ((var.get('x')&Js(15))==Js(0.0)):
            var.put('x', Js(4.0), '>>')
            var.put('r', Js(4.0), '+')
        if ((var.get('x')&Js(3.0))==Js(0.0)):
            var.put('x', Js(2.0), '>>')
            var.put('r', Js(2.0), '+')
        if ((var.get('x')&Js(1.0))==Js(0.0)):
            var.put('r',Js(var.get('r').to_number())+Js(1))
        return var.get('r')
    PyJsHoisted_lbit_.func_name = 'lbit'
    var.put('lbit', PyJsHoisted_lbit_)
    @Js
    def PyJsHoisted_bnGetLowestSetBit_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['i'])
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get(u"this").get('t')):
            try:
                if (var.get(u"this").get(var.get('i'))!=Js(0.0)):
                    return ((var.get('i')*var.get(u"this").get('DB'))+var.get('lbit')(var.get(u"this").get(var.get('i'))))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        if (var.get(u"this").get('s')<Js(0.0)):
            return (var.get(u"this").get('t')*var.get(u"this").get('DB'))
        return (-Js(1.0))
    PyJsHoisted_bnGetLowestSetBit_.func_name = 'bnGetLowestSetBit'
    var.put('bnGetLowestSetBit', PyJsHoisted_bnGetLowestSetBit_)
    @Js
    def PyJsHoisted_cbit_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        var.put('r', Js(0.0))
        while (var.get('x')!=Js(0.0)):
            var.put('x', (var.get('x')-Js(1.0)), '&')
            var.put('r',Js(var.get('r').to_number())+Js(1))
        return var.get('r')
    PyJsHoisted_cbit_.func_name = 'cbit'
    var.put('cbit', PyJsHoisted_cbit_)
    @Js
    def PyJsHoisted_bnBitCount_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'x', 'r'])
        var.put('r', Js(0.0))
        var.put('x', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get(u"this").get('t')):
            try:
                var.put('r', var.get('cbit')((var.get(u"this").get(var.get('i'))^var.get('x'))), '+')
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        return var.get('r')
    PyJsHoisted_bnBitCount_.func_name = 'bnBitCount'
    var.put('bnBitCount', PyJsHoisted_bnBitCount_)
    @Js
    def PyJsHoisted_bnTestBit_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'j'])
        var.put('j', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
        if (var.get('j')>=var.get(u"this").get('t')):
            return (var.get(u"this").get('s')!=Js(0.0))
        return ((var.get(u"this").get(var.get('j'))&(Js(1.0)<<(var.get('n')%var.get(u"this").get('DB'))))!=Js(0.0))
    PyJsHoisted_bnTestBit_.func_name = 'bnTestBit'
    var.put('bnTestBit', PyJsHoisted_bnTestBit_)
    @Js
    def PyJsHoisted_bnpChangeBit_(n, op, this, arguments, var=var):
        var = Scope({'n':n, 'op':op, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'op', 'r'])
        var.put('r', var.get('BigInteger').get('ONE').callprop('shiftLeft', var.get('n')))
        var.get(u"this").callprop('bitwiseTo', var.get('r'), var.get('op'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnpChangeBit_.func_name = 'bnpChangeBit'
    var.put('bnpChangeBit', PyJsHoisted_bnpChangeBit_)
    @Js
    def PyJsHoisted_bnSetBit_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get(u"this").callprop('changeBit', var.get('n'), var.get('op_or'))
    PyJsHoisted_bnSetBit_.func_name = 'bnSetBit'
    var.put('bnSetBit', PyJsHoisted_bnSetBit_)
    @Js
    def PyJsHoisted_bnClearBit_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get(u"this").callprop('changeBit', var.get('n'), var.get('op_andnot'))
    PyJsHoisted_bnClearBit_.func_name = 'bnClearBit'
    var.put('bnClearBit', PyJsHoisted_bnClearBit_)
    @Js
    def PyJsHoisted_bnFlipBit_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get(u"this").callprop('changeBit', var.get('n'), var.get('op_xor'))
    PyJsHoisted_bnFlipBit_.func_name = 'bnFlipBit'
    var.put('bnFlipBit', PyJsHoisted_bnFlipBit_)
    @Js
    def PyJsHoisted_bnpAddTo_(a, r, this, arguments, var=var):
        var = Scope({'a':a, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'i', 'a', 'm', 'c'])
        var.put('i', Js(0.0))
        var.put('c', Js(0.0))
        var.put('m', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
        while (var.get('i')<var.get('m')):
            var.put('c', (var.get(u"this").get(var.get('i'))+var.get('a').get(var.get('i'))), '+')
            var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
            var.put('c', var.get(u"this").get('DB'), '>>')
        if (var.get('a').get('t')<var.get(u"this").get('t')):
            var.put('c', var.get('a').get('s'), '+')
            while (var.get('i')<var.get(u"this").get('t')):
                var.put('c', var.get(u"this").get(var.get('i')), '+')
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                var.put('c', var.get(u"this").get('DB'), '>>')
            var.put('c', var.get(u"this").get('s'), '+')
        else:
            var.put('c', var.get(u"this").get('s'), '+')
            while (var.get('i')<var.get('a').get('t')):
                var.put('c', var.get('a').get(var.get('i')), '+')
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                var.put('c', var.get(u"this").get('DB'), '>>')
            var.put('c', var.get('a').get('s'), '+')
        var.get('r').put('s', ((-Js(1.0)) if (var.get('c')<Js(0.0)) else Js(0.0)))
        if (var.get('c')>Js(0.0)):
            var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), var.get('c'))
        else:
            if (var.get('c')<(-Js(1.0))):
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get(u"this").get('DV')+var.get('c')))
        var.get('r').put('t', var.get('i'))
        var.get('r').callprop('clamp')
    PyJsHoisted_bnpAddTo_.func_name = 'bnpAddTo'
    var.put('bnpAddTo', PyJsHoisted_bnpAddTo_)
    @Js
    def PyJsHoisted_bnAdd_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('addTo', var.get('a'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnAdd_.func_name = 'bnAdd'
    var.put('bnAdd', PyJsHoisted_bnAdd_)
    @Js
    def PyJsHoisted_bnSubtract_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('subTo', var.get('a'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnSubtract_.func_name = 'bnSubtract'
    var.put('bnSubtract', PyJsHoisted_bnSubtract_)
    @Js
    def PyJsHoisted_bnMultiply_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('multiplyTo', var.get('a'), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnMultiply_.func_name = 'bnMultiply'
    var.put('bnMultiply', PyJsHoisted_bnMultiply_)
    @Js
    def PyJsHoisted_bnDivide_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('divRemTo', var.get('a'), var.get('r'), var.get(u"null"))
        return var.get('r')
    PyJsHoisted_bnDivide_.func_name = 'bnDivide'
    var.put('bnDivide', PyJsHoisted_bnDivide_)
    @Js
    def PyJsHoisted_bnRemainder_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'r'])
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('divRemTo', var.get('a'), var.get(u"null"), var.get('r'))
        return var.get('r')
    PyJsHoisted_bnRemainder_.func_name = 'bnRemainder'
    var.put('bnRemainder', PyJsHoisted_bnRemainder_)
    @Js
    def PyJsHoisted_bnDivideAndRemainder_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'q', 'r'])
        var.put('q', var.get('nbi')())
        var.put('r', var.get('nbi')())
        var.get(u"this").callprop('divRemTo', var.get('a'), var.get('q'), var.get('r'))
        return var.get('Array').create(var.get('q'), var.get('r'))
    PyJsHoisted_bnDivideAndRemainder_.func_name = 'bnDivideAndRemainder'
    var.put('bnDivideAndRemainder', PyJsHoisted_bnDivideAndRemainder_)
    @Js
    def PyJsHoisted_bnpDMultiply_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        var.get(u"this").put(var.get(u"this").get('t'), var.get(u"this").callprop('am', Js(0.0), (var.get('n')-Js(1.0)), var.get(u"this"), Js(0.0), Js(0.0), var.get(u"this").get('t')))
        var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))
        var.get(u"this").callprop('clamp')
    PyJsHoisted_bnpDMultiply_.func_name = 'bnpDMultiply'
    var.put('bnpDMultiply', PyJsHoisted_bnpDMultiply_)
    @Js
    def PyJsHoisted_bnpDAddOffset_(n, w, this, arguments, var=var):
        var = Scope({'n':n, 'w':w, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'w'])
        while (var.get(u"this").get('t')<=var.get('w')):
            var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), Js(0.0))
        var.get(u"this").put(var.get('w'), var.get('n'), '+')
        while (var.get(u"this").get(var.get('w'))>=var.get(u"this").get('DV')):
            var.get(u"this").put(var.get('w'), var.get(u"this").get('DV'), '-')
            if (var.put('w',Js(var.get('w').to_number())+Js(1))>=var.get(u"this").get('t')):
                var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), Js(0.0))
            var.get(u"this").put(var.get('w'),Js(var.get(u"this").get(var.get('w')).to_number())+Js(1))
    PyJsHoisted_bnpDAddOffset_.func_name = 'bnpDAddOffset'
    var.put('bnpDAddOffset', PyJsHoisted_bnpDAddOffset_)
    @Js
    def PyJsHoisted_NullExp_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        pass
    PyJsHoisted_NullExp_.func_name = 'NullExp'
    var.put('NullExp', PyJsHoisted_NullExp_)
    @Js
    def PyJsHoisted_nNop_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x'])
        return var.get('x')
    PyJsHoisted_nNop_.func_name = 'nNop'
    var.put('nNop', PyJsHoisted_nNop_)
    @Js
    def PyJsHoisted_nMulTo_(x, y, r, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x', 'r'])
        var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
    PyJsHoisted_nMulTo_.func_name = 'nMulTo'
    var.put('nMulTo', PyJsHoisted_nMulTo_)
    @Js
    def PyJsHoisted_nSqrTo_(x, r, this, arguments, var=var):
        var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        var.get('x').callprop('squareTo', var.get('r'))
    PyJsHoisted_nSqrTo_.func_name = 'nSqrTo'
    var.put('nSqrTo', PyJsHoisted_nSqrTo_)
    @Js
    def PyJsHoisted_bnPow_(e, this, arguments, var=var):
        var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
        var.registers(['e'])
        return var.get(u"this").callprop('exp', var.get('e'), var.get('NullExp').create())
    PyJsHoisted_bnPow_.func_name = 'bnPow'
    var.put('bnPow', PyJsHoisted_bnPow_)
    @Js
    def PyJsHoisted_bnpMultiplyLowerTo_(a, n, r, this, arguments, var=var):
        var = Scope({'a':a, 'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['j', 'n', 'r', 'i', 'a'])
        var.put('i', var.get('Math').callprop('min', (var.get(u"this").get('t')+var.get('a').get('t')), var.get('n')))
        var.get('r').put('s', Js(0.0))
        var.get('r').put('t', var.get('i'))
        while (var.get('i')>Js(0.0)):
            var.get('r').put(var.put('i',Js(var.get('i').to_number())-Js(1)), Js(0.0))
        pass
        #for JS loop
        var.put('j', (var.get('r').get('t')-var.get(u"this").get('t')))
        while (var.get('i')<var.get('j')):
            try:
                var.get('r').put((var.get('i')+var.get(u"this").get('t')), var.get(u"this").callprop('am', Js(0.0), var.get('a').get(var.get('i')), var.get('r'), var.get('i'), Js(0.0), var.get(u"this").get('t')))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        #for JS loop
        var.put('j', var.get('Math').callprop('min', var.get('a').get('t'), var.get('n')))
        while (var.get('i')<var.get('j')):
            try:
                var.get(u"this").callprop('am', Js(0.0), var.get('a').get(var.get('i')), var.get('r'), var.get('i'), Js(0.0), (var.get('n')-var.get('i')))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        var.get('r').callprop('clamp')
    PyJsHoisted_bnpMultiplyLowerTo_.func_name = 'bnpMultiplyLowerTo'
    var.put('bnpMultiplyLowerTo', PyJsHoisted_bnpMultiplyLowerTo_)
    @Js
    def PyJsHoisted_bnpMultiplyUpperTo_(a, n, r, this, arguments, var=var):
        var = Scope({'a':a, 'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['n', 'r', 'i', 'a'])
        var.put('n',Js(var.get('n').to_number())-Js(1))
        var.put('i', var.get('r').put('t', ((var.get(u"this").get('t')+var.get('a').get('t'))-var.get('n'))))
        var.get('r').put('s', Js(0.0))
        while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
            var.get('r').put(var.get('i'), Js(0.0))
        #for JS loop
        var.put('i', var.get('Math').callprop('max', (var.get('n')-var.get(u"this").get('t')), Js(0.0)))
        while (var.get('i')<var.get('a').get('t')):
            try:
                var.get('r').put(((var.get(u"this").get('t')+var.get('i'))-var.get('n')), var.get(u"this").callprop('am', (var.get('n')-var.get('i')), var.get('a').get(var.get('i')), var.get('r'), Js(0.0), Js(0.0), ((var.get(u"this").get('t')+var.get('i'))-var.get('n'))))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        var.get('r').callprop('clamp')
        var.get('r').callprop('drShiftTo', Js(1.0), var.get('r'))
    PyJsHoisted_bnpMultiplyUpperTo_.func_name = 'bnpMultiplyUpperTo'
    var.put('bnpMultiplyUpperTo', PyJsHoisted_bnpMultiplyUpperTo_)
    @Js
    def PyJsHoisted_Barrett_(m, this, arguments, var=var):
        var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
        var.registers(['m'])
        var.get(u"this").put('r2', var.get('nbi')())
        var.get(u"this").put('q3', var.get('nbi')())
        var.get('BigInteger').get('ONE').callprop('dlShiftTo', (Js(2.0)*var.get('m').get('t')), var.get(u"this").get('r2'))
        var.get(u"this").put('mu', var.get(u"this").get('r2').callprop('divide', var.get('m')))
        var.get(u"this").put('m', var.get('m'))
    PyJsHoisted_Barrett_.func_name = 'Barrett'
    var.put('Barrett', PyJsHoisted_Barrett_)
    @Js
    def PyJsHoisted_barrettConvert_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        if ((var.get('x').get('s')<Js(0.0)) or (var.get('x').get('t')>(Js(2.0)*var.get(u"this").get('m').get('t')))):
            return var.get('x').callprop('mod', var.get(u"this").get('m'))
        else:
            if (var.get('x').callprop('compareTo', var.get(u"this").get('m'))<Js(0.0)):
                return var.get('x')
            else:
                var.put('r', var.get('nbi')())
                var.get('x').callprop('copyTo', var.get('r'))
                var.get(u"this").callprop('reduce', var.get('r'))
                return var.get('r')
    PyJsHoisted_barrettConvert_.func_name = 'barrettConvert'
    var.put('barrettConvert', PyJsHoisted_barrettConvert_)
    @Js
    def PyJsHoisted_barrettRevert_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x'])
        return var.get('x')
    PyJsHoisted_barrettRevert_.func_name = 'barrettRevert'
    var.put('barrettRevert', PyJsHoisted_barrettRevert_)
    @Js
    def PyJsHoisted_barrettReduce_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x'])
        var.get('x').callprop('drShiftTo', (var.get(u"this").get('m').get('t')-Js(1.0)), var.get(u"this").get('r2'))
        if (var.get('x').get('t')>(var.get(u"this").get('m').get('t')+Js(1.0))):
            var.get('x').put('t', (var.get(u"this").get('m').get('t')+Js(1.0)))
            var.get('x').callprop('clamp')
        var.get(u"this").get('mu').callprop('multiplyUpperTo', var.get(u"this").get('r2'), (var.get(u"this").get('m').get('t')+Js(1.0)), var.get(u"this").get('q3'))
        var.get(u"this").get('m').callprop('multiplyLowerTo', var.get(u"this").get('q3'), (var.get(u"this").get('m').get('t')+Js(1.0)), var.get(u"this").get('r2'))
        while (var.get('x').callprop('compareTo', var.get(u"this").get('r2'))<Js(0.0)):
            var.get('x').callprop('dAddOffset', Js(1.0), (var.get(u"this").get('m').get('t')+Js(1.0)))
        var.get('x').callprop('subTo', var.get(u"this").get('r2'), var.get('x'))
        while (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0)):
            var.get('x').callprop('subTo', var.get(u"this").get('m'), var.get('x'))
    PyJsHoisted_barrettReduce_.func_name = 'barrettReduce'
    var.put('barrettReduce', PyJsHoisted_barrettReduce_)
    @Js
    def PyJsHoisted_barrettSqrTo_(x, r, this, arguments, var=var):
        var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        var.get('x').callprop('squareTo', var.get('r'))
        var.get(u"this").callprop('reduce', var.get('r'))
    PyJsHoisted_barrettSqrTo_.func_name = 'barrettSqrTo'
    var.put('barrettSqrTo', PyJsHoisted_barrettSqrTo_)
    @Js
    def PyJsHoisted_barrettMulTo_(x, y, r, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x', 'r'])
        var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
        var.get(u"this").callprop('reduce', var.get('r'))
    PyJsHoisted_barrettMulTo_.func_name = 'barrettMulTo'
    var.put('barrettMulTo', PyJsHoisted_barrettMulTo_)
    @Js
    def PyJsHoisted_bnModPow_(e, m, this, arguments, var=var):
        var = Scope({'e':e, 'm':m, 'this':this, 'arguments':arguments}, var)
        var.registers(['is1', 'k1', 'k', 'j', 'r2', 'n', 'r', 'w', 'km', 't', 'e', 'z', 'g2', 'i', 'g', 'm'])
        var.put('i', var.get('e').callprop('bitLength'))
        var.put('r', var.get('nbv')(Js(1.0)))
        if (var.get('i')<=Js(0.0)):
            return var.get('r')
        else:
            if (var.get('i')<Js(18.0)):
                var.put('k', Js(1.0))
            else:
                if (var.get('i')<Js(48.0)):
                    var.put('k', Js(3.0))
                else:
                    if (var.get('i')<Js(144.0)):
                        var.put('k', Js(4.0))
                    else:
                        if (var.get('i')<Js(768.0)):
                            var.put('k', Js(5.0))
                        else:
                            var.put('k', Js(6.0))
        if (var.get('i')<Js(8.0)):
            var.put('z', var.get('Classic').create(var.get('m')))
        else:
            if var.get('m').callprop('isEven'):
                var.put('z', var.get('Barrett').create(var.get('m')))
            else:
                var.put('z', var.get('Montgomery').create(var.get('m')))
        var.put('g', var.get('Array').create())
        var.put('n', Js(3.0))
        var.put('k1', (var.get('k')-Js(1.0)))
        var.put('km', ((Js(1.0)<<var.get('k'))-Js(1.0)))
        var.get('g').put('1', var.get('z').callprop('convert', var.get(u"this")))
        if (var.get('k')>Js(1.0)):
            var.put('g2', var.get('nbi')())
            var.get('z').callprop('sqrTo', var.get('g').get('1'), var.get('g2'))
            while (var.get('n')<=var.get('km')):
                var.get('g').put(var.get('n'), var.get('nbi')())
                var.get('z').callprop('mulTo', var.get('g2'), var.get('g').get((var.get('n')-Js(2.0))), var.get('g').get(var.get('n')))
                var.put('n', Js(2.0), '+')
        var.put('j', (var.get('e').get('t')-Js(1.0)))
        var.put('is1', Js(True))
        var.put('r2', var.get('nbi')())
        var.put('i', (var.get('nbits')(var.get('e').get(var.get('j')))-Js(1.0)))
        while (var.get('j')>=Js(0.0)):
            if (var.get('i')>=var.get('k1')):
                var.put('w', ((var.get('e').get(var.get('j'))>>(var.get('i')-var.get('k1')))&var.get('km')))
            else:
                var.put('w', ((var.get('e').get(var.get('j'))&((Js(1.0)<<(var.get('i')+Js(1.0)))-Js(1.0)))<<(var.get('k1')-var.get('i'))))
                if (var.get('j')>Js(0.0)):
                    var.put('w', (var.get('e').get((var.get('j')-Js(1.0)))>>((var.get(u"this").get('DB')+var.get('i'))-var.get('k1'))), '|')
            var.put('n', var.get('k'))
            while ((var.get('w')&Js(1.0))==Js(0.0)):
                var.put('w', Js(1.0), '>>')
                var.put('n',Js(var.get('n').to_number())-Js(1))
            if (var.put('i', var.get('n'), '-')<Js(0.0)):
                var.put('i', var.get(u"this").get('DB'), '+')
                var.put('j',Js(var.get('j').to_number())-Js(1))
            if var.get('is1'):
                var.get('g').get(var.get('w')).callprop('copyTo', var.get('r'))
                var.put('is1', Js(False))
            else:
                while (var.get('n')>Js(1.0)):
                    var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
                    var.get('z').callprop('sqrTo', var.get('r2'), var.get('r'))
                    var.put('n', Js(2.0), '-')
                if (var.get('n')>Js(0.0)):
                    var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
                else:
                    var.put('t', var.get('r'))
                    var.put('r', var.get('r2'))
                    var.put('r2', var.get('t'))
                var.get('z').callprop('mulTo', var.get('r2'), var.get('g').get(var.get('w')), var.get('r'))
            while ((var.get('j')>=Js(0.0)) and ((var.get('e').get(var.get('j'))&(Js(1.0)<<var.get('i')))==Js(0.0))):
                var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
                var.put('t', var.get('r'))
                var.put('r', var.get('r2'))
                var.put('r2', var.get('t'))
                if (var.put('i',Js(var.get('i').to_number())-Js(1))<Js(0.0)):
                    var.put('i', (var.get(u"this").get('DB')-Js(1.0)))
                    var.put('j',Js(var.get('j').to_number())-Js(1))
        return var.get('z').callprop('revert', var.get('r'))
    PyJsHoisted_bnModPow_.func_name = 'bnModPow'
    var.put('bnModPow', PyJsHoisted_bnModPow_)
    @Js
    def PyJsHoisted_bnGCD_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['t', 'i', 'a', 'g', 'y', 'x'])
        var.put('x', (var.get(u"this").callprop('negate') if (var.get(u"this").get('s')<Js(0.0)) else var.get(u"this").callprop('clone')))
        var.put('y', (var.get('a').callprop('negate') if (var.get('a').get('s')<Js(0.0)) else var.get('a').callprop('clone')))
        if (var.get('x').callprop('compareTo', var.get('y'))<Js(0.0)):
            var.put('t', var.get('x'))
            var.put('x', var.get('y'))
            var.put('y', var.get('t'))
        var.put('i', var.get('x').callprop('getLowestSetBit'))
        var.put('g', var.get('y').callprop('getLowestSetBit'))
        if (var.get('g')<Js(0.0)):
            return var.get('x')
        if (var.get('i')<var.get('g')):
            var.put('g', var.get('i'))
        if (var.get('g')>Js(0.0)):
            var.get('x').callprop('rShiftTo', var.get('g'), var.get('x'))
            var.get('y').callprop('rShiftTo', var.get('g'), var.get('y'))
        while (var.get('x').callprop('signum')>Js(0.0)):
            if (var.put('i', var.get('x').callprop('getLowestSetBit'))>Js(0.0)):
                var.get('x').callprop('rShiftTo', var.get('i'), var.get('x'))
            if (var.put('i', var.get('y').callprop('getLowestSetBit'))>Js(0.0)):
                var.get('y').callprop('rShiftTo', var.get('i'), var.get('y'))
            if (var.get('x').callprop('compareTo', var.get('y'))>=Js(0.0)):
                var.get('x').callprop('subTo', var.get('y'), var.get('x'))
                var.get('x').callprop('rShiftTo', Js(1.0), var.get('x'))
            else:
                var.get('y').callprop('subTo', var.get('x'), var.get('y'))
                var.get('y').callprop('rShiftTo', Js(1.0), var.get('y'))
        if (var.get('g')>Js(0.0)):
            var.get('y').callprop('lShiftTo', var.get('g'), var.get('y'))
        return var.get('y')
    PyJsHoisted_bnGCD_.func_name = 'bnGCD'
    var.put('bnGCD', PyJsHoisted_bnGCD_)
    @Js
    def PyJsHoisted_bnpModInt_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['d', 'n', 'i', 'r'])
        if (var.get('n')<=Js(0.0)):
            return Js(0.0)
        var.put('d', (var.get(u"this").get('DV')%var.get('n')))
        var.put('r', ((var.get('n')-Js(1.0)) if (var.get(u"this").get('s')<Js(0.0)) else Js(0.0)))
        if (var.get(u"this").get('t')>Js(0.0)):
            if (var.get('d')==Js(0.0)):
                var.put('r', (var.get(u"this").get('0')%var.get('n')))
            else:
                #for JS loop
                var.put('i', (var.get(u"this").get('t')-Js(1.0)))
                while (var.get('i')>=Js(0.0)):
                    try:
                        var.put('r', (((var.get('d')*var.get('r'))+var.get(u"this").get(var.get('i')))%var.get('n')))
                    finally:
                            var.put('i',Js(var.get('i').to_number())-Js(1))
        return var.get('r')
    PyJsHoisted_bnpModInt_.func_name = 'bnpModInt'
    var.put('bnpModInt', PyJsHoisted_bnpModInt_)
    @Js
    def PyJsHoisted_bnModInverse_(m, this, arguments, var=var):
        var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
        var.registers(['v', 'd', 'b', 'ac', 'u', 'a', 'm', 'c'])
        var.put('ac', var.get('m').callprop('isEven'))
        if ((var.get(u"this").callprop('isEven') and var.get('ac')) or (var.get('m').callprop('signum')==Js(0.0))):
            return var.get('BigInteger').get('ZERO')
        var.put('u', var.get('m').callprop('clone'))
        var.put('v', var.get(u"this").callprop('clone'))
        var.put('a', var.get('nbv')(Js(1.0)))
        var.put('b', var.get('nbv')(Js(0.0)))
        var.put('c', var.get('nbv')(Js(0.0)))
        var.put('d', var.get('nbv')(Js(1.0)))
        while (var.get('u').callprop('signum')!=Js(0.0)):
            while var.get('u').callprop('isEven'):
                var.get('u').callprop('rShiftTo', Js(1.0), var.get('u'))
                if var.get('ac'):
                    if (var.get('a').callprop('isEven').neg() or var.get('b').callprop('isEven').neg()):
                        var.get('a').callprop('addTo', var.get(u"this"), var.get('a'))
                        var.get('b').callprop('subTo', var.get('m'), var.get('b'))
                    var.get('a').callprop('rShiftTo', Js(1.0), var.get('a'))
                else:
                    if var.get('b').callprop('isEven').neg():
                        var.get('b').callprop('subTo', var.get('m'), var.get('b'))
                var.get('b').callprop('rShiftTo', Js(1.0), var.get('b'))
            while var.get('v').callprop('isEven'):
                var.get('v').callprop('rShiftTo', Js(1.0), var.get('v'))
                if var.get('ac'):
                    if (var.get('c').callprop('isEven').neg() or var.get('d').callprop('isEven').neg()):
                        var.get('c').callprop('addTo', var.get(u"this"), var.get('c'))
                        var.get('d').callprop('subTo', var.get('m'), var.get('d'))
                    var.get('c').callprop('rShiftTo', Js(1.0), var.get('c'))
                else:
                    if var.get('d').callprop('isEven').neg():
                        var.get('d').callprop('subTo', var.get('m'), var.get('d'))
                var.get('d').callprop('rShiftTo', Js(1.0), var.get('d'))
            if (var.get('u').callprop('compareTo', var.get('v'))>=Js(0.0)):
                var.get('u').callprop('subTo', var.get('v'), var.get('u'))
                if var.get('ac'):
                    var.get('a').callprop('subTo', var.get('c'), var.get('a'))
                var.get('b').callprop('subTo', var.get('d'), var.get('b'))
            else:
                var.get('v').callprop('subTo', var.get('u'), var.get('v'))
                if var.get('ac'):
                    var.get('c').callprop('subTo', var.get('a'), var.get('c'))
                var.get('d').callprop('subTo', var.get('b'), var.get('d'))
        if (var.get('v').callprop('compareTo', var.get('BigInteger').get('ONE'))!=Js(0.0)):
            return var.get('BigInteger').get('ZERO')
        if (var.get('d').callprop('compareTo', var.get('m'))>=Js(0.0)):
            return var.get('d').callprop('subtract', var.get('m'))
        if (var.get('d').callprop('signum')<Js(0.0)):
            var.get('d').callprop('addTo', var.get('m'), var.get('d'))
        else:
            return var.get('d')
        if (var.get('d').callprop('signum')<Js(0.0)):
            return var.get('d').callprop('add', var.get('m'))
        else:
            return var.get('d')
    PyJsHoisted_bnModInverse_.func_name = 'bnModInverse'
    var.put('bnModInverse', PyJsHoisted_bnModInverse_)
    @Js
    def PyJsHoisted_bnIsProbablePrime_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['j', 't', 'i', 'm', 'x'])
        var.put('x', var.get(u"this").callprop('abs'))
        if ((var.get('x').get('t')==Js(1.0)) and (var.get('x').get('0')<=var.get('lowprimes').get((var.get('lowprimes').get('length')-Js(1.0))))):
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('lowprimes').get('length')):
                try:
                    if (var.get('x').get('0')==var.get('lowprimes').get(var.get('i'))):
                        return Js(True)
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(False)
        if var.get('x').callprop('isEven'):
            return Js(False)
        var.put('i', Js(1.0))
        while (var.get('i')<var.get('lowprimes').get('length')):
            var.put('m', var.get('lowprimes').get(var.get('i')))
            var.put('j', (var.get('i')+Js(1.0)))
            while ((var.get('j')<var.get('lowprimes').get('length')) and (var.get('m')<var.get('lplim'))):
                var.put('m', var.get('lowprimes').get((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))), '*')
            var.put('m', var.get('x').callprop('modInt', var.get('m')))
            while (var.get('i')<var.get('j')):
                if ((var.get('m')%var.get('lowprimes').get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))==Js(0.0)):
                    return Js(False)
        return var.get('x').callprop('millerRabin', var.get('t'))
    PyJsHoisted_bnIsProbablePrime_.func_name = 'bnIsProbablePrime'
    var.put('bnIsProbablePrime', PyJsHoisted_bnIsProbablePrime_)
    @Js
    def PyJsHoisted_bnpMillerRabin_(t, this, arguments, var=var):
        var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
        var.registers(['j', 'k', 'r', 't', 'i', 'a', 'n1', 'y'])
        var.put('n1', var.get(u"this").callprop('subtract', var.get('BigInteger').get('ONE')))
        var.put('k', var.get('n1').callprop('getLowestSetBit'))
        if (var.get('k')<=Js(0.0)):
            return Js(False)
        var.put('r', var.get('n1').callprop('shiftRight', var.get('k')))
        var.put('t', ((var.get('t')+Js(1.0))>>Js(1.0)))
        if (var.get('t')>var.get('lowprimes').get('length')):
            var.put('t', var.get('lowprimes').get('length'))
        var.put('a', var.get('nbi')())
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('t')):
            try:
                var.get('a').callprop('fromInt', var.get('lowprimes').get(var.get('i')))
                var.put('y', var.get('a').callprop('modPow', var.get('r'), var.get(u"this")))
                if ((var.get('y').callprop('compareTo', var.get('BigInteger').get('ONE'))!=Js(0.0)) and (var.get('y').callprop('compareTo', var.get('n1'))!=Js(0.0))):
                    var.put('j', Js(1.0))
                    while (((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))<var.get('k')) and (var.get('y').callprop('compareTo', var.get('n1'))!=Js(0.0))):
                        var.put('y', var.get('y').callprop('modPowInt', Js(2.0), var.get(u"this")))
                        if (var.get('y').callprop('compareTo', var.get('BigInteger').get('ONE'))==Js(0.0)):
                            return Js(False)
                    if (var.get('y').callprop('compareTo', var.get('n1'))!=Js(0.0)):
                        return Js(False)
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        return Js(True)
    PyJsHoisted_bnpMillerRabin_.func_name = 'bnpMillerRabin'
    var.put('bnpMillerRabin', PyJsHoisted_bnpMillerRabin_)
    var.put('canary', Js(244837814094590))
    var.put('j_lm', ((var.get('canary')&Js(16777215))==Js(15715070)))
    var.get('BigInteger').get('prototype').put('am', var.get('am2'))
    var.put('dbits', Js(30.0))
    var.get('BigInteger').get('prototype').put('DB', var.get('dbits'))
    var.get('BigInteger').get('prototype').put('DM', ((Js(1.0)<<var.get('dbits'))-Js(1.0)))
    var.get('BigInteger').get('prototype').put('DV', (Js(1.0)<<var.get('dbits')))
    var.put('BI_FP', Js(52.0))
    var.get('BigInteger').get('prototype').put('FV', var.get('Math').callprop('pow', Js(2.0), var.get('BI_FP')))
    var.get('BigInteger').get('prototype').put('F1', (var.get('BI_FP')-var.get('dbits')))
    var.get('BigInteger').get('prototype').put('F2', ((Js(2.0)*var.get('dbits'))-var.get('BI_FP')))
    var.put('BI_RM', Js('0123456789abcdefghijklmnopqrstuvwxyz'))
    var.put('BI_RC', var.get('Array').create())
    pass
    var.put('rr', Js('0').callprop('charCodeAt', Js(0.0)))
    #for JS loop
    var.put('vv', Js(0.0))
    while (var.get('vv')<=Js(9.0)):
        try:
            var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
        finally:
                var.put('vv',Js(var.get('vv').to_number())+Js(1))
    var.put('rr', Js('a').callprop('charCodeAt', Js(0.0)))
    #for JS loop
    var.put('vv', Js(10.0))
    while (var.get('vv')<Js(36.0)):
        try:
            var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
        finally:
                var.put('vv',Js(var.get('vv').to_number())+Js(1))
    var.put('rr', Js('A').callprop('charCodeAt', Js(0.0)))
    #for JS loop
    var.put('vv', Js(10.0))
    while (var.get('vv')<Js(36.0)):
        try:
            var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
        finally:
                var.put('vv',Js(var.get('vv').to_number())+Js(1))

    var.get('Classic').get('prototype').put('convert', var.get('cConvert'))
    var.get('Classic').get('prototype').put('revert', var.get('cRevert'))
    var.get('Classic').get('prototype').put('reduce', var.get('cReduce'))
    var.get('Classic').get('prototype').put('mulTo', var.get('cMulTo'))
    var.get('Classic').get('prototype').put('sqrTo', var.get('cSqrTo'))
    var.get('Montgomery').get('prototype').put('convert', var.get('montConvert'))
    var.get('Montgomery').get('prototype').put('revert', var.get('montRevert'))
    var.get('Montgomery').get('prototype').put('reduce', var.get('montReduce'))
    var.get('Montgomery').get('prototype').put('mulTo', var.get('montMulTo'))
    var.get('Montgomery').get('prototype').put('sqrTo', var.get('montSqrTo'))
    var.get('BigInteger').get('prototype').put('copyTo', var.get('bnpCopyTo'))
    var.get('BigInteger').get('prototype').put('fromInt', var.get('bnpFromInt'))
    var.get('BigInteger').get('prototype').put('fromString', var.get('bnpFromString'))
    var.get('BigInteger').get('prototype').put('clamp', var.get('bnpClamp'))
    var.get('BigInteger').get('prototype').put('dlShiftTo', var.get('bnpDLShiftTo'))
    var.get('BigInteger').get('prototype').put('drShiftTo', var.get('bnpDRShiftTo'))
    var.get('BigInteger').get('prototype').put('lShiftTo', var.get('bnpLShiftTo'))
    var.get('BigInteger').get('prototype').put('rShiftTo', var.get('bnpRShiftTo'))
    var.get('BigInteger').get('prototype').put('subTo', var.get('bnpSubTo'))
    var.get('BigInteger').get('prototype').put('multiplyTo', var.get('bnpMultiplyTo'))
    var.get('BigInteger').get('prototype').put('squareTo', var.get('bnpSquareTo'))
    var.get('BigInteger').get('prototype').put('divRemTo', var.get('bnpDivRemTo'))
    var.get('BigInteger').get('prototype').put('invDigit', var.get('bnpInvDigit'))
    var.get('BigInteger').get('prototype').put('isEven', var.get('bnpIsEven'))
    var.get('BigInteger').get('prototype').put('exp', var.get('bnpExp'))
    var.get('BigInteger').get('prototype').put('toString', var.get('bnToString'))
    var.get('BigInteger').get('prototype').put('negate', var.get('bnNegate'))
    var.get('BigInteger').get('prototype').put('abs', var.get('bnAbs'))
    var.get('BigInteger').get('prototype').put('compareTo', var.get('bnCompareTo'))
    var.get('BigInteger').get('prototype').put('bitLength', var.get('bnBitLength'))
    var.get('BigInteger').get('prototype').put('mod', var.get('bnMod'))
    var.get('BigInteger').get('prototype').put('modPowInt', var.get('bnModPowInt'))
    var.get('BigInteger').put('ZERO', var.get('nbv')(Js(0.0)))
    var.get('BigInteger').put('ONE', var.get('nbv')(Js(1.0)))
    var.get('NullExp').get('prototype').put('convert', var.get('nNop'))
    var.get('NullExp').get('prototype').put('revert', var.get('nNop'))
    var.get('NullExp').get('prototype').put('mulTo', var.get('nMulTo'))
    var.get('NullExp').get('prototype').put('sqrTo', var.get('nSqrTo'))
    var.get('Barrett').get('prototype').put('convert', var.get('barrettConvert'))
    var.get('Barrett').get('prototype').put('revert', var.get('barrettRevert'))
    var.get('Barrett').get('prototype').put('reduce', var.get('barrettReduce'))
    var.get('Barrett').get('prototype').put('mulTo', var.get('barrettMulTo'))
    var.get('Barrett').get('prototype').put('sqrTo', var.get('barrettSqrTo'))
    var.put('lowprimes', Js([Js(2.0), Js(3.0), Js(5.0), Js(7.0), Js(11.0), Js(13.0), Js(17.0), Js(19.0), Js(23.0), Js(29.0), Js(31.0), Js(37.0), Js(41.0), Js(43.0), Js(47.0), Js(53.0), Js(59.0), Js(61.0), Js(67.0), Js(71.0), Js(73.0), Js(79.0), Js(83.0), Js(89.0), Js(97.0), Js(101.0), Js(103.0), Js(107.0), Js(109.0), Js(113.0), Js(127.0), Js(131.0), Js(137.0), Js(139.0), Js(149.0), Js(151.0), Js(157.0), Js(163.0), Js(167.0), Js(173.0), Js(179.0), Js(181.0), Js(191.0), Js(193.0), Js(197.0), Js(199.0), Js(211.0), Js(223.0), Js(227.0), Js(229.0), Js(233.0), Js(239.0), Js(241.0), Js(251.0), Js(257.0), Js(263.0), Js(269.0), Js(271.0), Js(277.0), Js(281.0), Js(283.0), Js(293.0), Js(307.0), Js(311.0), Js(313.0), Js(317.0), Js(331.0), Js(337.0), Js(347.0), Js(349.0), Js(353.0), Js(359.0), Js(367.0), Js(373.0), Js(379.0), Js(383.0), Js(389.0), Js(397.0), Js(401.0), Js(409.0), Js(419.0), Js(421.0), Js(431.0), Js(433.0), Js(439.0), Js(443.0), Js(449.0), Js(457.0), Js(461.0), Js(463.0), Js(467.0), Js(479.0), Js(487.0), Js(491.0), Js(499.0), Js(503.0), Js(509.0)]))
    var.put('lplim', ((Js(1.0)<<Js(26.0))/var.get('lowprimes').get((var.get('lowprimes').get('length')-Js(1.0)))))
    var.get('BigInteger').get('prototype').put('chunkSize', var.get('bnpChunkSize'))
    var.get('BigInteger').get('prototype').put('toRadix', var.get('bnpToRadix'))
    var.get('BigInteger').get('prototype').put('fromRadix', var.get('bnpFromRadix'))
    var.get('BigInteger').get('prototype').put('fromNumber', var.get('bnpFromNumber'))
    var.get('BigInteger').get('prototype').put('bitwiseTo', var.get('bnpBitwiseTo'))
    var.get('BigInteger').get('prototype').put('changeBit', var.get('bnpChangeBit'))
    var.get('BigInteger').get('prototype').put('addTo', var.get('bnpAddTo'))
    var.get('BigInteger').get('prototype').put('dMultiply', var.get('bnpDMultiply'))
    var.get('BigInteger').get('prototype').put('dAddOffset', var.get('bnpDAddOffset'))
    var.get('BigInteger').get('prototype').put('multiplyLowerTo', var.get('bnpMultiplyLowerTo'))
    var.get('BigInteger').get('prototype').put('multiplyUpperTo', var.get('bnpMultiplyUpperTo'))
    var.get('BigInteger').get('prototype').put('modInt', var.get('bnpModInt'))
    var.get('BigInteger').get('prototype').put('millerRabin', var.get('bnpMillerRabin'))
    var.get('BigInteger').get('prototype').put('clone', var.get('bnClone'))
    var.get('BigInteger').get('prototype').put('intValue', var.get('bnIntValue'))
    var.get('BigInteger').get('prototype').put('byteValue', var.get('bnByteValue'))
    var.get('BigInteger').get('prototype').put('shortValue', var.get('bnShortValue'))
    var.get('BigInteger').get('prototype').put('signum', var.get('bnSigNum'))
    var.get('BigInteger').get('prototype').put('toByteArray', var.get('bnToByteArray'))
    var.get('BigInteger').get('prototype').put('equals', var.get('bnEquals'))
    var.get('BigInteger').get('prototype').put('min', var.get('bnMin'))
    var.get('BigInteger').get('prototype').put('max', var.get('bnMax'))
    var.get('BigInteger').get('prototype').put('and', var.get('bnAnd'))
    var.get('BigInteger').get('prototype').put('or', var.get('bnOr'))
    var.get('BigInteger').get('prototype').put('xor', var.get('bnXor'))
    var.get('BigInteger').get('prototype').put('andNot', var.get('bnAndNot'))
    var.get('BigInteger').get('prototype').put('not', var.get('bnNot'))
    var.get('BigInteger').get('prototype').put('shiftLeft', var.get('bnShiftLeft'))
    var.get('BigInteger').get('prototype').put('shiftRight', var.get('bnShiftRight'))
    var.get('BigInteger').get('prototype').put('getLowestSetBit', var.get('bnGetLowestSetBit'))
    var.get('BigInteger').get('prototype').put('bitCount', var.get('bnBitCount'))
    var.get('BigInteger').get('prototype').put('testBit', var.get('bnTestBit'))
    var.get('BigInteger').get('prototype').put('setBit', var.get('bnSetBit'))
    var.get('BigInteger').get('prototype').put('clearBit', var.get('bnClearBit'))
    var.get('BigInteger').get('prototype').put('flipBit', var.get('bnFlipBit'))
    var.get('BigInteger').get('prototype').put('add', var.get('bnAdd'))
    var.get('BigInteger').get('prototype').put('subtract', var.get('bnSubtract'))
    var.get('BigInteger').get('prototype').put('multiply', var.get('bnMultiply'))
    var.get('BigInteger').get('prototype').put('divide', var.get('bnDivide'))
    var.get('BigInteger').get('prototype').put('remainder', var.get('bnRemainder'))
    var.get('BigInteger').get('prototype').put('divideAndRemainder', var.get('bnDivideAndRemainder'))
    var.get('BigInteger').get('prototype').put('modPow', var.get('bnModPow'))
    var.get('BigInteger').get('prototype').put('modInverse', var.get('bnModInverse'))
    var.get('BigInteger').get('prototype').put('pow', var.get('bnPow'))
    var.get('BigInteger').get('prototype').put('gcd', var.get('bnGCD'))
    var.get('BigInteger').get('prototype').put('isProbablePrime', var.get('bnIsProbablePrime'))
    @Js
    def PyJs_anonymous_0_(PyJsArg_246d6f64756c75735f686578_, PyJsArg_24656e6372797074696f6e4578706f6e656e745f686578_, this, arguments, var=var):
        var = Scope({'$modulus_hex':PyJsArg_246d6f64756c75735f686578_, '$encryptionExponent_hex':PyJsArg_24656e6372797074696f6e4578706f6e656e745f686578_, 'this':this, 'arguments':arguments}, var)
        var.registers(['$encryptionExponent_hex', '$modulus_hex'])
        var.get(u"this").put('modulus', var.get('BigInteger').create(var.get('$modulus_hex'), Js(16.0)))
        var.get(u"this").put('encryptionExponent', var.get('BigInteger').create(var.get('$encryptionExponent_hex'), Js(16.0)))
    PyJs_anonymous_0_._set_name('anonymous')
    var.put('RSAPublicKey', PyJs_anonymous_0_)
    @Js
    def PyJs_anonymous_1_(PyJsArg_24696e707574_, this, arguments, var=var):
        var = Scope({'$input':PyJsArg_24696e707574_, 'this':this, 'arguments':arguments}, var)
        var.registers(['$enc4', '$enc2', '$enc3', '$input', '$enc1', '$i', '$chr1', '$chr3', '$output', '$chr2'])
        if var.get('$input').neg():
            return Js(False)
        var.put('$output', Js(''))
        pass
        pass
        var.put('$i', Js(0.0))
        while 1:
            var.put('$chr1', var.get('$input').callprop('charCodeAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1))))
            var.put('$chr2', var.get('$input').callprop('charCodeAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1))))
            var.put('$chr3', var.get('$input').callprop('charCodeAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1))))
            var.put('$enc1', (var.get('$chr1')>>Js(2.0)))
            var.put('$enc2', (((var.get('$chr1')&Js(3.0))<<Js(4.0))|(var.get('$chr2')>>Js(4.0))))
            var.put('$enc3', (((var.get('$chr2')&Js(15.0))<<Js(2.0))|(var.get('$chr3')>>Js(6.0))))
            var.put('$enc4', (var.get('$chr3')&Js(63.0)))
            if var.get('isNaN')(var.get('$chr2')):
                var.put('$enc3', var.put('$enc4', Js(64.0)))
            else:
                if var.get('isNaN')(var.get('$chr3')):
                    var.put('$enc4', Js(64.0))
            var.put('$output', (((var.get(u"this").get('base64').callprop('charAt', var.get('$enc1'))+var.get(u"this").get('base64').callprop('charAt', var.get('$enc2')))+var.get(u"this").get('base64').callprop('charAt', var.get('$enc3')))+var.get(u"this").get('base64').callprop('charAt', var.get('$enc4'))), '+')
            if not (var.get('$i')<var.get('$input').get('length')):
                break
        return var.get('$output')
    PyJs_anonymous_1_._set_name('anonymous')
    @Js
    def PyJs_anonymous_2_(PyJsArg_24696e707574_, this, arguments, var=var):
        var = Scope({'$input':PyJsArg_24696e707574_, 'this':this, 'arguments':arguments}, var)
        var.registers(['$enc4', '$enc2', '$enc3', '$input', '$enc1', '$i', '$output'])
        if var.get('$input').neg():
            return Js(False)
        var.put('$input', var.get('$input').callprop('replace', JsRegExp('/[^A-Za-z0-9\\+\\/\\=]/g'), Js('')))
        var.put('$output', Js(''))
        pass
        var.put('$i', Js(0.0))
        while 1:
            var.put('$enc1', var.get(u"this").get('base64').callprop('indexOf', var.get('$input').callprop('charAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1)))))
            var.put('$enc2', var.get(u"this").get('base64').callprop('indexOf', var.get('$input').callprop('charAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1)))))
            var.put('$enc3', var.get(u"this").get('base64').callprop('indexOf', var.get('$input').callprop('charAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1)))))
            var.put('$enc4', var.get(u"this").get('base64').callprop('indexOf', var.get('$input').callprop('charAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1)))))
            var.put('$output', var.get('String').callprop('fromCharCode', ((var.get('$enc1')<<Js(2.0))|(var.get('$enc2')>>Js(4.0)))), '+')
            if (var.get('$enc3')!=Js(64.0)):
                var.put('$output', var.get('String').callprop('fromCharCode', (((var.get('$enc2')&Js(15.0))<<Js(4.0))|(var.get('$enc3')>>Js(2.0)))), '+')
            if (var.get('$enc4')!=Js(64.0)):
                var.put('$output', var.get('String').callprop('fromCharCode', (((var.get('$enc3')&Js(3.0))<<Js(6.0))|var.get('$enc4'))), '+')
            if not (var.get('$i')<var.get('$input').get('length')):
                break
        return var.get('$output')
    PyJs_anonymous_2_._set_name('anonymous')
    var.put('Base64', Js({'base64':Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='),'encode':PyJs_anonymous_1_,'decode':PyJs_anonymous_2_}))
    @Js
    def PyJs_anonymous_3_(PyJsArg_24696e707574_, this, arguments, var=var):
        var = Scope({'$input':PyJsArg_24696e707574_, 'this':this, 'arguments':arguments}, var)
        var.registers(['$output', '$k', '$i', '$input'])
        if var.get('$input').neg():
            return Js(False)
        var.put('$output', Js(''))
        pass
        var.put('$i', Js(0.0))
        while 1:
            var.put('$k', var.get('$input').callprop('charCodeAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1))))
            var.put('$output', (var.get(u"this").get('hex').callprop('charAt', ((var.get('$k')>>Js(4.0))&Js(15)))+var.get(u"this").get('hex').callprop('charAt', (var.get('$k')&Js(15)))), '+')
            if not (var.get('$i')<var.get('$input').get('length')):
                break
        return var.get('$output')
    PyJs_anonymous_3_._set_name('anonymous')
    @Js
    def PyJs_anonymous_4_(PyJsArg_24696e707574_, this, arguments, var=var):
        var = Scope({'$input':PyJsArg_24696e707574_, 'this':this, 'arguments':arguments}, var)
        var.registers(['$output', '$i', '$input'])
        if var.get('$input').neg():
            return Js(False)
        var.put('$input', var.get('$input').callprop('replace', JsRegExp('/[^0-9abcdef]/g'), Js('')))
        var.put('$output', Js(''))
        var.put('$i', Js(0.0))
        while 1:
            var.put('$output', var.get('String').callprop('fromCharCode', (((var.get(u"this").get('hex').callprop('indexOf', var.get('$input').callprop('charAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1))))<<Js(4.0))&Js(240))|(var.get(u"this").get('hex').callprop('indexOf', var.get('$input').callprop('charAt', (var.put('$i',Js(var.get('$i').to_number())+Js(1))-Js(1))))&Js(15)))), '+')
            if not (var.get('$i')<var.get('$input').get('length')):
                break
        return var.get('$output')
    PyJs_anonymous_4_._set_name('anonymous')
    var.put('Hex', Js({'hex':Js('0123456789abcdef'),'encode':PyJs_anonymous_3_,'decode':PyJs_anonymous_4_}))
    @Js
    def PyJs_anonymous_5_(PyJsArg_246d6f64756c75735f686578_, PyJsArg_246578706f6e656e745f686578_, this, arguments, var=var):
        var = Scope({'$modulus_hex':PyJsArg_246d6f64756c75735f686578_, '$exponent_hex':PyJsArg_246578706f6e656e745f686578_, 'this':this, 'arguments':arguments}, var)
        var.registers(['$exponent_hex', '$modulus_hex'])
        return var.get('RSAPublicKey').create(var.get('$modulus_hex'), var.get('$exponent_hex'))
    PyJs_anonymous_5_._set_name('anonymous')
    @Js
    def PyJs_anonymous_6_(PyJsArg_2464617461_, PyJsArg_247075626b6579_, this, arguments, var=var):
        var = Scope({'$data':PyJsArg_2464617461_, '$pubkey':PyJsArg_247075626b6579_, 'this':this, 'arguments':arguments}, var)
        var.registers(['$pubkey', '$data'])
        if var.get('$pubkey').neg():
            return Js(False)
        var.put('$data', var.get(u"this").callprop('pkcs1pad2', var.get('$data'), ((var.get('$pubkey').get('modulus').callprop('bitLength')+Js(7.0))>>Js(3.0))))
        if var.get('$data').neg():
            return Js(False)
        var.put('$data', var.get('$data').callprop('modPowInt', var.get('$pubkey').get('encryptionExponent'), var.get('$pubkey').get('modulus')))
        if var.get('$data').neg():
            return Js(False)
        var.put('$data', var.get('$data').callprop('toString', Js(16.0)))
        if ((var.get('$data').get('length')&Js(1.0))==Js(1.0)):
            var.put('$data', (Js('0')+var.get('$data')))
        return var.get('Base64').callprop('encode', var.get('Hex').callprop('decode', var.get('$data')))
    PyJs_anonymous_6_._set_name('anonymous')
    @Js
    def PyJs_anonymous_7_(PyJsArg_2464617461_, PyJsArg_246b657973697a65_, this, arguments, var=var):
        var = Scope({'$data':PyJsArg_2464617461_, '$keysize':PyJsArg_246b657973697a65_, 'this':this, 'arguments':arguments}, var)
        var.registers(['$keysize', '$i', '$data', '$buffer'])
        if (var.get('$keysize')<(var.get('$data').get('length')+Js(11.0))):
            return var.get(u"null")
        var.put('$buffer', Js([]))
        var.put('$i', (var.get('$data').get('length')-Js(1.0)))
        while ((var.get('$i')>=Js(0.0)) and (var.get('$keysize')>Js(0.0))):
            var.get('$buffer').put(var.put('$keysize',Js(var.get('$keysize').to_number())-Js(1)), var.get('$data').callprop('charCodeAt', (var.put('$i',Js(var.get('$i').to_number())-Js(1))+Js(1))))
        var.get('$buffer').put(var.put('$keysize',Js(var.get('$keysize').to_number())-Js(1)), Js(0.0))
        while (var.get('$keysize')>Js(2.0)):
            var.get('$buffer').put(var.put('$keysize',Js(var.get('$keysize').to_number())-Js(1)), (var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(254.0)))+Js(1.0)))
        var.get('$buffer').put(var.put('$keysize',Js(var.get('$keysize').to_number())-Js(1)), Js(2.0))
        var.get('$buffer').put(var.put('$keysize',Js(var.get('$keysize').to_number())-Js(1)), Js(0.0))
        return var.get('BigInteger').create(var.get('$buffer'))
    PyJs_anonymous_7_._set_name('anonymous')
    var.put('RSA', Js({'getPublicKey':PyJs_anonymous_5_,'encrypt':PyJs_anonymous_6_,'pkcs1pad2':PyJs_anonymous_7_}))
    var.put('modulus', varDict["mod"])
    var.put('exponent', varDict["exp"])
    var.put('pubKey', var.get('RSA').callprop('getPublicKey', var.get('modulus'), var.get('exponent')))
    var.put('username', 'username')
    var.put('password', varDict["password"])
    var.put('encryptedPassword', var.get('RSA').callprop('encrypt', var.get('password'), var.get('pubKey')))
    return str(var.get('encryptedPassword')).strip("'")


# Add lib to the module scope
test = var.to_python()