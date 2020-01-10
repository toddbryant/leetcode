/*
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 *
 * Straightforward recursive solution.
 */
public class Solution {
    public void ParenHelper(int n, int open, int closed, string curString, IList<string> strings) {
        if(open==n && closed==n) // Base case
        { 
            strings.Add(curString);
        }   
        else
        {
            if (open < n) // open a new paren
                ParenHelper(n, open+1, closed, curString + "(", strings);
            if (closed < open) // there's something to close
                ParenHelper(n, open, closed+1, curString + ")", strings);
        }
    }
    
    public IList<string> GenerateParenthesis(int n) {
        var strings = new List<string>();
        ParenHelper(n, 0, 0, "", strings);
        return strings;
    }
}
