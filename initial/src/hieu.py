def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(getIntLn),[])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_var_decl(self):
        input = """int a,b,c;"""
        expect = "Program([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_var_decl1(self):
        input = """float b;"""
        expect = "Program([VarDecl(Id(b),FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_var_array_decl(self):
        input = """int a[5];"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,5))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_var_array_decl1(self):
        input = """int a[5],b;"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,5)),VarDecl(Id(b),IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_var_array_decl2(self):
        input = """int a[5],b;
string e;"""
        expect = "Program([VarDecl(Id(a),ArrayType(IntType,5)),VarDecl(Id(b),IntType),VarDecl(Id(e),StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    
    def test_func_decl(self):
        input = """float foo(int a, int b){
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],FloatType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_func_decl1(self):
        input = """boolean main(string a1, float arr[],boolean flag){
}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(Id(a1),StringType),VarDecl(Id(arr),ArrayTypePointer(FloatType)),VarDecl(Id(flag),BoolType)],BoolType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_func_var_decl(self):
        input = """float a[3], b;
int[] foo(string a1, float arr[],int b[]){
}"""
        expect = "Program([VarDecl(Id(a),ArrayType(FloatType,3)),VarDecl(Id(b),FloatType),FuncDecl(Id(foo),[VarDecl(Id(a1),StringType),VarDecl(Id(arr),ArrayTypePointer(FloatType)),VarDecl(Id(b),ArrayTypePointer(IntType))],ArrayTypePointer(IntType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_stmt_simple(self):
        input = """
int main(){
    continue;
    return;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Continue(),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_stmt_simple1(self):
        input = """
float foo(float a){
    break;
    int a, arr[3];
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType)],FloatType,Block([Break(),VarDecl(Id(a),IntType),VarDecl(Id(arr),ArrayType(IntType,3))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,312)) 
    def test_stmt_simple2(self):
        input = """
float foo(float a){
    (1+2);
    return 1+2;
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType)],FloatType,Block([BinaryOp(+,IntLiteral(1),IntLiteral(2)),Return(BinaryOp(+,IntLiteral(1),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,313)) 
    def test_stmt_simple3(self):
        input = """
void foo(float a){
    if (a == 1){
        break;
    }
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType)],VoidType,Block([If(BinaryOp(==,Id(a),IntLiteral(1)),Block([Break()]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_stmt_simple4(self):
        input = """
void foo(){
    for(i=1;i<2;i=i+1) continue;
}"""
        expect = "Program([FuncDecl(Id(foo),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_stmt_simple5(self):
        input = """
void foo(int a, int b){
    do a+1; while a=a*a;
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],VoidType,Block([Dowhile([BinaryOp(+,Id(a),IntLiteral(1))],BinaryOp(=,Id(a),BinaryOp(*,Id(a),Id(a))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_stmt_simple6(self):
        input = """
void foo(int a, int b){
    int a,b,c,d;
    if (a ==1) {
        a=3;
    }
}"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],VoidType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(d),IntType),If(BinaryOp(==,Id(a),IntLiteral(1)),Block([BinaryOp(=,Id(a),IntLiteral(3))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_arraycell_simple(self):
        input = """
int main(){
    a[ 1 + x] = true && false;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,ArrayCell(Id(a),BinaryOp(+,IntLiteral(1),Id(x))),BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,318)) 
    def test_funcall_simple(self):
        input = """
int main(){
    foo(a,1.23);
    string arr[5];
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(foo),[Id(a),FloatLiteral(1.23)]),VarDecl(Id(arr),ArrayType(StringType,5))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_funcall_simple1(self):
        input = """
int main(){
    do{
    }
    if (str == "string")
        return -1;
    while (1.2e3 >= x);
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([]),If(BinaryOp(==,Id(str),StringLiteral(string)),Return(UnaryOp(-,IntLiteral(1))))],BinaryOp(>=,FloatLiteral(1200.0),Id(x)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_funcall_simple2(self):
        input = """
int x,y,arr[6];
boolean flag;
void main(){
    for(x=0;y=x % -2.32;x=x+1){
        arr[x]= !1;
    }
}"""
        expect = "Program([VarDecl(Id(x),IntType),VarDecl(Id(y),IntType),VarDecl(Id(arr),ArrayType(IntType,6)),VarDecl(Id(flag),BoolType),FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(x),IntLiteral(0));BinaryOp(=,Id(y),BinaryOp(%,Id(x),UnaryOp(-,FloatLiteral(2.32))));BinaryOp(=,Id(x),BinaryOp(+,Id(x),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(arr),Id(x)),UnaryOp(!,IntLiteral(1)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_exp_simple(self):
        input = """
        int foo (float a, int arr[]) 
        {
            int a , b , c ;
            float a[5],d ;
            string str;
            a = b + c;
            if (a > b) a = a -2;
            if(false) a = a+2;
        }
"""
        expect = """Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(arr),ArrayTypePointer(IntType))],IntType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),VarDecl(Id(a),ArrayType(FloatType,5)),VarDecl(Id(d),FloatType),VarDecl(Id(str),StringType),BinaryOp(=,Id(a),BinaryOp(+,Id(b),Id(c))),If(BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BinaryOp(-,Id(a),IntLiteral(2)))),If(BooleanLiteral(false),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(2))))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_func_call(self):

        input = """
        int main(){
            func((arr[i])[j]);
        }
        """
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(func),[ArrayCell(ArrayCell(Id(arr),Id(i)),Id(j))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_simple_program2(self):
        input = """
        int main(){
            do { }
            while((arr[i])[j]);
        }
        """
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([])],ArrayCell(ArrayCell(Id(arr),Id(i)),Id(j)))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_simple_program3(self):
        input = """boolean func1(boolean arg1, int arg2, float arr[]){}"""
        expect = """Program([FuncDecl(Id(func1),[VarDecl(Id(arg1),BoolType),VarDecl(Id(arg2),IntType),VarDecl(Id(arr),ArrayTypePointer(FloatType))],BoolType,Block([]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_func_decl3(self):
        input = """float func_test(string str[], int a){
    a = a + 1;
    func_test(str[2], a+2);            
}"""
        expect = """Program([FuncDecl(Id(func_test),[VarDecl(Id(str),ArrayTypePointer(StringType)),VarDecl(Id(a),IntType)],FloatType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),CallExpr(Id(func_test),[ArrayCell(Id(str),IntLiteral(2)),BinaryOp(+,Id(a),IntLiteral(2))])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_func_decl4(self):
        input = """int __foo(){
    if(var!=0) print("hello");
}"""
        expect ="""Program([FuncDecl(Id(__foo),[],IntType,Block([If(BinaryOp(!=,Id(var),IntLiteral(0)),CallExpr(Id(print),[StringLiteral(hello)]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_do_while_stmt(self):
        """test do while stmt"""
        input = """void main() {
    do{
    print("statement 1");
    }
    {
    print("statement 2");
    }
    while (true);
}
"""
        expect = """Program([FuncDecl(Id(main),[],VoidType,Block([Dowhile([Block([CallExpr(Id(print),[StringLiteral(statement 1)])]),Block([CallExpr(Id(print),[StringLiteral(statement 2)])])],BooleanLiteral(true))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_do_while_stmt2(self):
        """test do while stmt"""
        input = """int main () {
    /* local variable definition */
    int a;
    a = 0;
    /* do loop execution */
    do {
        printf("value of a: ", a);
        a = a + 1;
    }while( a < 20 );
    return 0;
}
"""
        expect="""Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),IntLiteral(0)),Dowhile([Block([CallExpr(Id(printf),[StringLiteral(value of a: ),Id(a)]),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])],BinaryOp(<,Id(a),IntLiteral(20))),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_do_while_stmt4(self):
        """test do while stmt"""
        input = """int main () {
    do{
        //comment1
        a=b=c==d;
    }while(false);
}
string foo(string a){
    //comment2
    a = k;
    return a;
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(=,Id(b),BinaryOp(==,Id(c),Id(d))))])],BooleanLiteral(false))])),FuncDecl(Id(foo),[VarDecl(Id(a),StringType)],StringType,Block([BinaryOp(=,Id(a),Id(k)),Return(Id(a))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_do_while_stmt5(self):
        """"""
        input = """int main () {
    if(-5.0)
        do{
            !a;
            string a,b,arr[4];
        }while(arr[true]);
    else
        print("error");
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([If(UnaryOp(-,FloatLiteral(5.0)),Dowhile([Block([UnaryOp(!,Id(a)),VarDecl(Id(a),StringType),VarDecl(Id(b),StringType),VarDecl(Id(arr),ArrayType(StringType,4))])],ArrayCell(Id(arr),BooleanLiteral(true))),CallExpr(Id(print),[StringLiteral(error)]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_for_stmt(self):
        """test for stmt"""
        input = """boolean ptr[4],_a,_b;
int func() {
    for( i =0;i <=5;i=i+1)
        func2(ptr[2],_a,_b);     
}
"""
        expect = """Program([VarDecl(Id(ptr),ArrayType(BoolType,4)),VarDecl(Id(_a),BoolType),VarDecl(Id(_b),BoolType),FuncDecl(Id(func),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<=,Id(i),IntLiteral(5));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(func2),[ArrayCell(Id(ptr),IntLiteral(2)),Id(_a),Id(_b)]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,332)) 
    def test_for_stmt2(self):
        """test for stmt"""
        input = """float a;
string b;
int[] func(int a, string b) {
    for(!2;-3;5){
        a=a+b;
        func(a,b);
    }    
}
"""
        expect = """Program([VarDecl(Id(a),FloatType),VarDecl(Id(b),StringType),FuncDecl(Id(func),[VarDecl(Id(a),IntType),VarDecl(Id(b),StringType)],ArrayTypePointer(IntType),Block([For(UnaryOp(!,IntLiteral(2));UnaryOp(-,IntLiteral(3));IntLiteral(5);Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),Id(b))),CallExpr(Id(func),[Id(a),Id(b)])]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_for_stmt3(self):
        input = """int main()
{
    int num, count, sum;
    sum =0;
    printf("Enter a positive integer: ");
    scanf("%d", num);
    // for loop terminates when num is less than count
    for(count = 1; count <= num; count = count + 1)
    {
        sum =sum + count;
    }
    printf("Sum = %d", sum);
    return 0;
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(num),IntType),VarDecl(Id(count),IntType),VarDecl(Id(sum),IntType),BinaryOp(=,Id(sum),IntLiteral(0)),CallExpr(Id(printf),[StringLiteral(Enter a positive integer: )]),CallExpr(Id(scanf),[StringLiteral(%d),Id(num)]),For(BinaryOp(=,Id(count),IntLiteral(1));BinaryOp(<=,Id(count),Id(num));BinaryOp(=,Id(count),BinaryOp(+,Id(count),IntLiteral(1)));Block([BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),Id(count)))])),CallExpr(Id(printf),[StringLiteral(Sum = %d),Id(sum)]),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_all_stmt(self):
        input = """string[] ABS(string a, int w[]){
    {
    }
    {    
    }
}
"""
        expect = """Program([FuncDecl(Id(ABS),[VarDecl(Id(a),StringType),VarDecl(Id(w),ArrayTypePointer(IntType))],ArrayTypePointer(StringType),Block([Block([]),Block([])]))])"""    
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_all_stmt1(self):
        """test all stmt"""
        input = """int[] ABS(int a, float b){
    int a;
    a =8;
    if(-5 == a){
        a = a+1;
    }
    else
        continue;
    return a;
}
"""
        expect = """Program([FuncDecl(Id(ABS),[VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType)],ArrayTypePointer(IntType),Block([VarDecl(Id(a),IntType),BinaryOp(=,Id(a),IntLiteral(8)),If(BinaryOp(==,UnaryOp(-,IntLiteral(5)),Id(a)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))]),Continue()),Return(Id(a))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_all_stmt2(self):
        """test all stmt"""
        input = """int main()
{
    int i;
    float number, sum;
    sum = 0.0 ;
    for(i=1; i <= 10;i = i *i)
    {
        printf("Enter a n%d: ",i);
        scanf("%lf", number);
        if(number < 0.0)
        {
            continue;
        }
        sum =sum+ number; 
    }
    printf("Sum = %.2lf",sum);
    return 0;
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(i),IntType),VarDecl(Id(number),FloatType),VarDecl(Id(sum),FloatType),BinaryOp(=,Id(sum),FloatLiteral(0.0)),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(*,Id(i),Id(i)));Block([CallExpr(Id(printf),[StringLiteral(Enter a n%d: ),Id(i)]),CallExpr(Id(scanf),[StringLiteral(%lf),Id(number)]),If(BinaryOp(<,Id(number),FloatLiteral(0.0)),Block([Continue()])),BinaryOp(=,Id(sum),BinaryOp(+,Id(sum),Id(number)))])),CallExpr(Id(printf),[StringLiteral(Sum = %.2lf),Id(sum)]),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_all_stmt3(self):
        """test all stmt"""
        input = """int main(){
    do
        {
        statement1;
        if (condition)
            break;
        statement2;
    }while (test_condition);
}
"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([Id(statement1),If(Id(condition),Break()),Id(statement2)])],Id(test_condition))]))])"""           
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_all_stmt4(self):
        input = """int trim(string s[])
{
    int n;
    for (n = strlen(s)-1; n >= 0; n= n /2)
    if (s[n] != " " && s[n] != "\\t" && s[n] != "\\n")
        break;
    s[n+1] = "0";
    return n;
}"""
        expect = """Program([FuncDecl(Id(trim),[VarDecl(Id(s),ArrayTypePointer(StringType))],IntType,Block([VarDecl(Id(n),IntType),For(BinaryOp(=,Id(n),BinaryOp(-,CallExpr(Id(strlen),[Id(s)]),IntLiteral(1)));BinaryOp(>=,Id(n),IntLiteral(0));BinaryOp(=,Id(n),BinaryOp(/,Id(n),IntLiteral(2)));If(BinaryOp(&&,BinaryOp(&&,BinaryOp(!=,ArrayCell(Id(s),Id(n)),StringLiteral( )),BinaryOp(!=,ArrayCell(Id(s),Id(n)),StringLiteral(\\t))),BinaryOp(!=,ArrayCell(Id(s),Id(n)),StringLiteral(\\n))),Break())),BinaryOp(=,ArrayCell(Id(s),BinaryOp(+,Id(n),IntLiteral(1))),StringLiteral(0)),Return(Id(n))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_all_stmt5(self):
        input = """int main()
{
    float number1;
    number1=13.5;
    float number2;
    number2 = 12.4;
    printf("number1 = %f\\n", number1);
    printf("number2 = %lf", number2);
    return 0;
}"""
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(Id(number1),FloatType),BinaryOp(=,Id(number1),FloatLiteral(13.5)),VarDecl(Id(number2),FloatType),BinaryOp(=,Id(number2),FloatLiteral(12.4)),CallExpr(Id(printf),[StringLiteral(number1 = %f\\n),Id(number1)]),CallExpr(Id(printf),[StringLiteral(number2 = %lf),Id(number2)]),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_for_stmt4(self):
        """nested for loop"""
        input = """int[] main(int i, float a[])
{
    for (i=0; i<2; i=-i+1 )
    {
	    for (j=0; j<4; j= j%2)
	    {
	        printf("%d, %d\\n",i ,j);
	    }
    }
   return 0;
}"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(Id(i),IntType),VarDecl(Id(a),ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(2));BinaryOp(=,Id(i),BinaryOp(+,UnaryOp(-,Id(i)),IntLiteral(1)));Block([For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<,Id(j),IntLiteral(4));BinaryOp(=,Id(j),BinaryOp(%,Id(j),IntLiteral(2)));Block([CallExpr(Id(printf),[StringLiteral(%d, %d\\n),Id(i),Id(j)])]))])),Return(IntLiteral(0))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_func_call1(self):
        """test function call"""
        input = """int main()
{
    func1(foo(x%2),foo(foo(x+3,5.01*0.e-2),foo("string \\\\")));
    return 0;
}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(func1),[CallExpr(Id(foo),[BinaryOp(%,Id(x),IntLiteral(2))]),CallExpr(Id(foo),[CallExpr(Id(foo),[BinaryOp(+,Id(x),IntLiteral(3)),BinaryOp(*,FloatLiteral(5.01),FloatLiteral(0.0))]),CallExpr(Id(foo),[StringLiteral(string \\\\)])])]),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,342))