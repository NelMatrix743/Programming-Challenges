class Solution {
	
	// Converting Int to String
    fun isPalindrome(x: Int): Boolean {
        val str: String = x.toString()
        var a: Int = 0
        var b: Int = str.length - 1
        while(a < b){
            if(str[a] != str[b])
                return false
            a++; b--
        }
        return true
    }
    
}