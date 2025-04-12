class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        from collections import Counter
        #precompute factorials up to n
        factorials = [1] * (n + 1)
        for i in range(2, n + 1):
            factorials[i] = factorials[i - 1] * i
            
        def permutation_with_repetition(lenght,counts_tuple):
            num = factorials[lenght]
            den = 1
            for count in counts_tuple:
                if count > 1:
                    den *= factorials[count]
            
            #ensure integer division
            if den == 0: return 0
            return num // den
        m = (n + 1) // 2
        start = 10**(m - 1) if m > 0 else 0
        if n==1: start = 0
        end = 10**m
        
        good_signatures = set()
        
        for first_half_num in range(start,end):
            first_half_str = str(first_half_num)
            if len(first_half_str) < m:
                first_half_str = '0' * (m - len(first_half_str)) + first_half_str 
            
            second_half_str = first_half_str[:n-m][::-1]
            p_str = first_half_str + second_half_str
            
            #skip if leading zero
            if n > 1 and p_str[0] == '0':
                continue
            
            p = int(p_str)
            # check divisibility by k
            if p % k == 0:
                #calculate digit counts(signature)
                counts = Counter(p_str)
                signature_list = [0] * 10
                for digit_char, count in counts.items():
                    if digit_char.isdigit():
                        signature_list[int(digit_char)] = count
                    #add tuple representation to set
                good_signatures.add(tuple(signature_list))
        
        total_good_integers = 0
        for sig_tuple in good_signatures:
            total_perms = permutation_with_repetition(n, sig_tuple)
            count_zero = sig_tuple[0]
            
            if count_zero == 0:
                valid_perms = total_perms
            else:
                invalid_counts_list = list(sig_tuple)
                invalid_counts_list[0] -= 1
                invalid_perms = permutation_with_repetition(n-1, tuple(invalid_counts_list))
                valid_perms = total_perms - invalid_perms
            
            total_good_integers += valid_perms
        return total_good_integers
                
            
