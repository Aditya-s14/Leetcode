bool isValid(char* s) {
    char stack[10000]; 
    int top = -1;        // Initialize the stack pointer

    for (int i = 0; s[i] != '\0'; i++) {
        // Push opening brackets to the stack
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack[++top] = s[i];
        } else {
            // If stack is empty or brackets don't match, return false
            if (top == -1)
            {
                return false;
            }
            if ((s[i] == ')' && stack[top] != '(') ||
                (s[i] == '}' && stack[top] != '{') ||
                (s[i] == ']' && stack[top] != '[')) {
                return false;
            }
            top--;  // Pop the top element
        }
    }

    // If the stack is empty, all brackets matched correctly
    return top == -1;
 
    
}