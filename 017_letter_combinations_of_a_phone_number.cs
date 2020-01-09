public class Solution
{
    static Dictionary<char, string> KEYPAD = new Dictionary<char, string>()
    {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"},
        {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
        {'8', "tuv"}, {'9', "wxyz"}
    };

    public void RecurseThroughCombinations(IList<string> combos, ref string digits, StringBuilder currentWord)
    {
        if (currentWord.Length < digits.Length)
        {
            foreach (char c in KEYPAD[digits[currentWord.Length]])
            {
                currentWord.Append(c);
                RecurseThroughCombinations(combos, ref digits, currentWord);
                currentWord.Remove(currentWord.Length - 1, 1);
            }
        }
        else if(currentWord.Length > 0)
        {
            combos.Add(currentWord.ToString());
        }
    }

    public IList<string> LetterCombinations(string digits)
    {
        IList<string> values = new List<string>();
        var currentWord = new StringBuilder();
        RecurseThroughCombinations(values, ref digits, currentWord);

        return values;
    }
}
