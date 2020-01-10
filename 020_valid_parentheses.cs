/*
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
 * determine if the input string is valid.
 * An input string is valid if:
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Note that an empty string is also considered valid.
 *
 * Not much to say here; this is solved easily with a stack.
*/
public class Solution {
    public bool IsValid(string s) {
        var stack = new Stack<char>();
        char lastOpen;
        
        foreach(char c in s) {
            if(c=='(' || c=='{' || c=='[') // Open bracket
                stack.Push(c);
            else { // Close bracket
                if(!stack.TryPop(out lastOpen)) // stack was empty
                    return false;
                if(c==')' && lastOpen!='(')
                    return false;
                if(c=='}' && lastOpen!='{') 
                    return false;
                if(c==']' && lastOpen!='[')
                    return false;
            }
        }
        
        return stack.Count == 0;
    }
}
