import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {}"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))

    # def test_more_complex_program(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(4);
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    # def test_call_without_parameter(self):
    #     """More complex program"""
    #     input = """int main () {
    #         getIntLn();
    #     }"""
    #     expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([CallExpr(Id("getIntLn"),[])]))]))
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))
   
    # test var declaration
    def test_vardeclaration(self):
        input = """int a,b,c[10],d;
                float e;
                string w,q;"""
        # expect = str(Program([VarDecl("a",IntType()),VarDecl("b",IntType()),VarDecl("c",ArrayType(10,IntType())),VarDecl("d",IntType()),VarDecl("e",FloatType()),VarDecl("w",StringType()),VarDecl("q",StringType())]))
        expect="Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,10)),VarDecl(d,IntType),VarDecl(e,FloatType),VarDecl(w,StringType),VarDecl(q,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,400))
    def test_vardeclaration_1(self):
        input = """int a,b,c[10],d;
                float e[23],p;"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(c,ArrayType(IntType,10)),VarDecl(d,IntType),VarDecl(e,ArrayType(FloatType,23)),VarDecl(p,FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,401)) 
    def test_vardeclaration_2(self):
        input = """boolean a,c[5];
                string e[23],p[7];"""
        expect = "Program([VarDecl(a,BoolType),VarDecl(c,ArrayType(BoolType,5)),VarDecl(e,ArrayType(StringType,23)),VarDecl(p,ArrayType(StringType,7))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,402))
    def test_vardeclaration_3(self):
        input = """boolean c[5],a;
                float b;"""
        expect = "Program([VarDecl(c,ArrayType(BoolType,5)),VarDecl(a,BoolType),VarDecl(b,FloatType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,403))
    def test_vardeclaration_4(self):
        input = """boolean a[10],b,c[5];
                string p[7],d;"""
        expect = "Program([VarDecl(a,ArrayType(BoolType,10)),VarDecl(b,BoolType),VarDecl(c,ArrayType(BoolType,5)),VarDecl(p,ArrayType(StringType,7)),VarDecl(d,StringType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,404))

    #test function declaration
    def test_funcdeclaration(self):
        input = """int main(){}"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,405))
    def test_funcdeclaration_1(self):
        input = """int main(float b,string arr[]){}"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(b,FloatType),VarDecl(arr,ArrayTypePointer(StringType))],IntType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,406))
    def test_funcdeclaration_2(self):
        input = """int main(){
            string a[10],b;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(StringType,10)),VarDecl(b,StringType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,407))
    def test_funcdeclaration_3(self):
        input = """int main(){
            string x[20],y;
            float k;
            boolean j;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(x,ArrayType(StringType,20)),VarDecl(y,StringType),VarDecl(k,FloatType),VarDecl(j,BoolType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,408))
    def test_funcdeclaration_4(self):
        input = """int[] main(){}"""
        expect = "Program([FuncDecl(Id(main),[],ArrayTypePointer(IntType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,409))
    def test_funcdeclaration_5(self):
        input = """float[] main(int a,float x[]){
            string b,z[20];
            boolean r;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,IntType),VarDecl(x,ArrayTypePointer(FloatType))],ArrayTypePointer(FloatType),Block([VarDecl(b,StringType),VarDecl(z,ArrayType(StringType,20)),VarDecl(r,BoolType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,410))
    def test_funcdeclaration_6(self):
        input = """void main(){}"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,411))
    def test_funcdeclaration_7(self):
        input = """void main(){
            int r,s,t[10];
            float y;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(r,IntType),VarDecl(s,IntType),VarDecl(t,ArrayType(IntType,10)),VarDecl(y,FloatType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,412))
    def test_funcdeclaration_8(self):
        input = """void main(int hello[],float PPL){
            int s,t[10];
            string minh;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(hello,ArrayTypePointer(IntType)),VarDecl(PPL,FloatType)],VoidType,Block([VarDecl(s,IntType),VarDecl(t,ArrayType(IntType,10)),VarDecl(minh,StringType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,413))
    def test_funcdeclaration_9(self):
        input = """
        float add(int a,int b){
            int c;
            float result;
        }
        void main(float PPL){
            int s,t[10];
        }"""
        expect = "Program([FuncDecl(Id(add),[VarDecl(a,IntType),VarDecl(b,IntType)],FloatType,Block([VarDecl(c,IntType),VarDecl(result,FloatType)])),FuncDecl(Id(main),[VarDecl(PPL,FloatType)],VoidType,Block([VarDecl(s,IntType),VarDecl(t,ArrayType(IntType,10))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,414))
    def test_funcdeclaration_10(self):
        input = """
        string chain(string a,string b){
            string result;
        }
        float add(int a,int b){
            int c;
            float result;
        }
        void main(float PPL){
            int s,t[10];
        }"""
        expect = "Program([FuncDecl(Id(chain),[VarDecl(a,StringType),VarDecl(b,StringType)],StringType,Block([VarDecl(result,StringType)])),FuncDecl(Id(add),[VarDecl(a,IntType),VarDecl(b,IntType)],FloatType,Block([VarDecl(c,IntType),VarDecl(result,FloatType)])),FuncDecl(Id(main),[VarDecl(PPL,FloatType)],VoidType,Block([VarDecl(s,IntType),VarDecl(t,ArrayType(IntType,10))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,415))

    #test if statement
    def test_if_statement(self):
        input = """int main(){
            int a,b;
            if(a){
                break;
            }
            else
                a=a+1;
            b>c=d;
            
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),If(Id(a),Block([Break()]),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))),BinaryOp(=,BinaryOp(>,Id(b),Id(c)),Id(d))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,416))
    def test_if_statement_1(self):
        input = """int main(){
            int a,b;
            if(a>10){
                a=a+1;
                b>c=a;
                b;
            }
            return;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),If(BinaryOp(>,Id(a),IntLiteral(10)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,BinaryOp(>,Id(b),Id(c)),Id(a)),Id(b)])),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,417))
    def test_if_statement_2(self):
        input = """int main(){
            a[4];
            if(true) return false;
            if(0.5) return z;
            if(1e2) break;
        }"""
        # expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([ArrayCell(Id("a"),IntLiteral(4)),If(BooleanLiteral(True),Return(BooleanLiteral(False))),If(FloatLiteral(0.5),Return(Id("z"))),If(FloatLiteral(100.0),Break())]))]))
        expect="Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(Id(a),IntLiteral(4)),If(BooleanLiteral(true),Return(BooleanLiteral(false))),If(FloatLiteral(0.5),Return(Id(z))),If(FloatLiteral(100.0),Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,418))
    def test_if_statement_3(self):
        input = """string a,b;
        void main(){
            if(true && a > 5) a[foo()]=0;
            if(0.5+a==9) return true;
            if(1e2<=a) break;
        }"""
        # expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType()),FuncDecl(Id("main"),[],VoidType(),Block([If(BinaryOp("&&",BooleanLiteral(True),BinaryOp(">",Id("a"),IntLiteral(5))),BinaryOp("=",ArrayCell(Id("a"),CallExpr(Id("foo"),[])),IntLiteral(0))),If(BinaryOp("==",BinaryOp("+",FloatLiteral(0.5),Id("a")),IntLiteral(9)),Return(BooleanLiteral(True))),If(BinaryOp("<=",FloatLiteral(100.0),Id("a")),Break())]))]))
        expect="Program([VarDecl(a,StringType),VarDecl(b,StringType),FuncDecl(Id(main),[],VoidType,Block([If(BinaryOp(&&,BooleanLiteral(true),BinaryOp(>,Id(a),IntLiteral(5))),BinaryOp(=,ArrayCell(Id(a),CallExpr(Id(foo),[])),IntLiteral(0))),If(BinaryOp(==,BinaryOp(+,FloatLiteral(0.5),Id(a)),IntLiteral(9)),Return(BooleanLiteral(true))),If(BinaryOp(<=,FloatLiteral(100.0),Id(a)),Break())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,419))
    def test_if_statement_4(self):
        input = """string a,b;
        int main(){
            if(a>b){ a =a + 1;
            break;
            continue;
            }
            else{
                a=-b;
            }
        }"""
        expect = "Program([VarDecl(a,StringType),VarDecl(b,StringType),FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(a),Id(b)),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),Break(),Continue()]),Block([BinaryOp(=,Id(a),UnaryOp(-,Id(b)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,420))
    def test_if_statement_5(self):
        input = """string a,b;
        int main(){
            int a[10];
            if(a>b) a=a+1; else if(a<=c) return;
            if(true) a=false; else a>b;
        }"""
        expect = "Program([VarDecl(a,StringType),VarDecl(b,StringType),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(IntType,10)),If(BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(<=,Id(a),Id(c)),Return())),If(BooleanLiteral(true),BinaryOp(=,Id(a),BooleanLiteral(false)),BinaryOp(>,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,421))
    def test_if_statement_6(self):
        input = """string x,y;
        int main(){
            string a[10];
            a[a[5]]=true;
            if(a>b) a=a+1; else if(a<=c) return; else a<=b;
        }"""
        expect = "Program([VarDecl(x,StringType),VarDecl(y,StringType),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(StringType,10)),BinaryOp(=,ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(5))),BooleanLiteral(true)),If(BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(<=,Id(a),Id(c)),Return(),BinaryOp(<=,Id(a),Id(b))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,422))
    def test_if_statement_7(self):
        input = """string x,y;
        float a(){}
        int main(){
            string a[10];
            a[a[5]]=true;
            if(a>b) a=true; else if((a<=c)>d) return "o"; else a<=(b+5);
        }"""
        expect = "Program([VarDecl(x,StringType),VarDecl(y,StringType),FuncDecl(Id(a),[],FloatType,Block([])),FuncDecl(Id(main),[],IntType,Block([VarDecl(a,ArrayType(StringType,10)),BinaryOp(=,ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(5))),BooleanLiteral(true)),If(BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BinaryOp(>,BinaryOp(<=,Id(a),Id(c)),Id(d)),Return(StringLiteral(o)),BinaryOp(<=,Id(a),BinaryOp(+,Id(b),IntLiteral(5)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,423))
    def test_if_statement_8(self):
        input = """string x,y;
        int main(){
            if(c>d/a) return;
            else {
                a=a[a>b-c];
            }
        }"""
        expect = "Program([VarDecl(x,StringType),VarDecl(y,StringType),FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(c),BinaryOp(/,Id(d),Id(a))),Return(),Block([BinaryOp(=,Id(a),ArrayCell(Id(a),BinaryOp(>,Id(a),BinaryOp(-,Id(b),Id(c)))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,424))
    def test_if_statement_9(self):
        input = """string x,y;
        float[] PPL(){
            if(c<=d/a) return;
            else {
                a=b[99>g[10]]-a[a>b-c];
            }
        }"""
        expect = "Program([VarDecl(x,StringType),VarDecl(y,StringType),FuncDecl(Id(PPL),[],ArrayTypePointer(FloatType),Block([If(BinaryOp(<=,Id(c),BinaryOp(/,Id(d),Id(a))),Return(),Block([BinaryOp(=,Id(a),BinaryOp(-,ArrayCell(Id(b),BinaryOp(>,IntLiteral(99),ArrayCell(Id(g),IntLiteral(10)))),ArrayCell(Id(a),BinaryOp(>,Id(a),BinaryOp(-,Id(b),Id(c))))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,425))

    #test expression
    def test_expression(self):
        input = """int main(){
            a=a+1;
            b+c=d>e;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),BinaryOp(=,BinaryOp(+,Id(b),Id(c)),BinaryOp(>,Id(d),Id(e)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,426))
    def test_expression_1(self):
        input = """float foo(string a, int b){
            int a,b[10];
            string str[4];
        }
        int a(){
            a(a+b>c,a[a+b]);
        }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,StringType),VarDecl(b,IntType)],FloatType,Block([VarDecl(a,IntType),VarDecl(b,ArrayType(IntType,10)),VarDecl(str,ArrayType(StringType,4))])),FuncDecl(Id(a),[],IntType,Block([CallExpr(Id(a),[BinaryOp(>,BinaryOp(+,Id(a),Id(b)),Id(c)),ArrayCell(Id(a),BinaryOp(+,Id(a),Id(b)))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,427))
    def test_expression_2(self):
        input = """int test(){
            if(a>4) return;
            i+2;
            i=i+4;
            z>=5+2;
            if(b) return z+2;
        }"""
        expect = "Program([FuncDecl(Id(test),[],IntType,Block([If(BinaryOp(>,Id(a),IntLiteral(4)),Return()),BinaryOp(+,Id(i),IntLiteral(2)),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(4))),BinaryOp(>=,Id(z),BinaryOp(+,IntLiteral(5),IntLiteral(2))),If(Id(b),Return(BinaryOp(+,Id(z),IntLiteral(2))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,428))
    def test_expression_3(self):
        input = """int test(){
            int a;
            a=a+4*6+3>5;
            a/2=p/c+3*"hello"-d;
        }"""
        expect = "Program([FuncDecl(Id(test),[],IntType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BinaryOp(>,BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(*,IntLiteral(4),IntLiteral(6))),IntLiteral(3)),IntLiteral(5))),BinaryOp(=,BinaryOp(/,Id(a),IntLiteral(2)),BinaryOp(-,BinaryOp(+,BinaryOp(/,Id(p),Id(c)),BinaryOp(*,IntLiteral(3),StringLiteral(hello))),Id(d)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,429))
    def test_expression_4(self):
        input = """float PPLmain(){
            if( a==b && a!=c){
                a=b>=c;
                a=c;
            }
        }"""
        expect = "Program([FuncDecl(Id(PPLmain),[],FloatType,Block([If(BinaryOp(&&,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(a),Id(c))),Block([BinaryOp(=,Id(a),BinaryOp(>=,Id(b),Id(c))),BinaryOp(=,Id(a),Id(c))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,430))
    def test_expression_5(self):
        input = """void main(){
            foo(2)[3+x]=a[b[2]]+3;
            c[d[e+g]]=foo(a[9]+c[9[c-g]]);
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),BinaryOp(+,IntLiteral(3),Id(x))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLiteral(2))),IntLiteral(3))),BinaryOp(=,ArrayCell(Id(c),ArrayCell(Id(d),BinaryOp(+,Id(e),Id(g)))),CallExpr(Id(foo),[BinaryOp(+,ArrayCell(Id(a),IntLiteral(9)),ArrayCell(Id(c),ArrayCell(IntLiteral(9),BinaryOp(-,Id(c),Id(g)))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,431))
    def test_expression_6(self):
        input = """void main(int a[],float b,string c){
            array[a[a[c]+b]]=c*b-d/a;
            x<=y || a == b ;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(b,FloatType),VarDecl(c,StringType)],VoidType,Block([BinaryOp(=,ArrayCell(Id(array),ArrayCell(Id(a),BinaryOp(+,ArrayCell(Id(a),Id(c)),Id(b)))),BinaryOp(-,BinaryOp(*,Id(c),Id(b)),BinaryOp(/,Id(d),Id(a)))),BinaryOp(||,BinaryOp(<=,Id(x),Id(y)),BinaryOp(==,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,432))
    def test_expression_7(self):
        input = """void main(int a[],string c){
            x<=y || a == b ;
            rational(g+5*p[20]);
            print("result"+rational);
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(c,StringType)],VoidType,Block([BinaryOp(||,BinaryOp(<=,Id(x),Id(y)),BinaryOp(==,Id(a),Id(b))),CallExpr(Id(rational),[BinaryOp(+,Id(g),BinaryOp(*,IntLiteral(5),ArrayCell(Id(p),IntLiteral(20))))]),CallExpr(Id(print),[BinaryOp(+,StringLiteral(result),Id(rational))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,433))
    def test_expression_8(self):
        input = """void PPLmain(int a[],string c){
            x<=y || a == b || a=true && b+c || false;
        }"""
        expect = "Program([FuncDecl(Id(PPLmain),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(c,StringType)],VoidType,Block([BinaryOp(=,BinaryOp(||,BinaryOp(||,BinaryOp(<=,Id(x),Id(y)),BinaryOp(==,Id(a),Id(b))),Id(a)),BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BinaryOp(+,Id(b),Id(c))),BooleanLiteral(false)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,434))
    def test_expression_9(self):
        input = """void PPLmain(string c){
            true || x >= (y || a=true) && b+c || false;
        }"""
        expect = "Program([FuncDecl(Id(PPLmain),[VarDecl(c,StringType)],VoidType,Block([BinaryOp(||,BinaryOp(||,BooleanLiteral(true),BinaryOp(&&,BinaryOp(>=,Id(x),BinaryOp(=,BinaryOp(||,Id(y),Id(a)),BooleanLiteral(true))),BinaryOp(+,Id(b),Id(c)))),BooleanLiteral(false))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,435))
    
    #test for statement
    def test_for_statement(self):
        input = """int main(){
            for(i=0;i<10;i=i+1){
                if(true) return;
                return;
                a=a+i;
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BooleanLiteral(true),Return()),Return(),BinaryOp(=,Id(a),BinaryOp(+,Id(a),Id(i)))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,436))
    def test_for_statement_1(self):
        input = """float a(){
            int a[9],i;
            for(i=0;i<9;i=i+1){
                a[i]="PPL Lover";
            }
            print("successful");
        }"""
        expect = "Program([FuncDecl(Id(a),[],FloatType,Block([VarDecl(a,ArrayType(IntType,9)),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(9));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),StringLiteral(PPL Lover))])),CallExpr(Id(print),[StringLiteral(successful)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,437))
    def test_for_statement_2(self):
        input = """float a(){
            int a[9],i;
            for(i=0;i<9;i=i+1){
                if(i+1==9){
                    a[i]=a[0];
                    break;
                }
                a[i]=a[i+1];
            }
            print("PPL pass successful");
        }"""
        expect = "Program([FuncDecl(Id(a),[],FloatType,Block([VarDecl(a,ArrayType(IntType,9)),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(9));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(+,Id(i),IntLiteral(1)),IntLiteral(9)),Block([BinaryOp(=,ArrayCell(Id(a),Id(i)),ArrayCell(Id(a),IntLiteral(0))),Break()])),BinaryOp(=,ArrayCell(Id(a),Id(i)),ArrayCell(Id(a),BinaryOp(+,Id(i),IntLiteral(1))))])),CallExpr(Id(print),[StringLiteral(PPL pass successful)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,438))
    def test_for_statement_3(self):
        input = """boolean mainPPL(){
            int a[9],i;
            for(i=8;i>=0;i=i+2){
                if(i==false)
                    return true;
                return false;
            }
        }"""
        expect = "Program([FuncDecl(Id(mainPPL),[],BoolType,Block([VarDecl(a,ArrayType(IntType,9)),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(8));BinaryOp(>=,Id(i),IntLiteral(0));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(2)));Block([If(BinaryOp(==,Id(i),BooleanLiteral(false)),Return(BooleanLiteral(true))),Return(BooleanLiteral(false))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,439))

    #test do while statement
    def test_dowhile_statement(self):
        input = """int main(){
            do a=a+1; while a<10;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,440))
    def test_dowhile_statement_1(self):
        input = """int main(){
            int a,b;
            do a=a+1; while a<10;
            return true;
            float c;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,IntType),VarDecl(b,IntType),Dowhile([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))],BinaryOp(<,Id(a),IntLiteral(10))),Return(BooleanLiteral(true)),VarDecl(c,FloatType)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,441))
    def test_dowhile_statement_2(self):
        input = """void main(string args[]){
            do{ 
                a+b=1;
                if(a>b) break;
                else return; 
            }while a<b+c;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([Dowhile([Block([BinaryOp(=,BinaryOp(+,Id(a),Id(b)),IntLiteral(1)),If(BinaryOp(>,Id(a),Id(b)),Break(),Return())])],BinaryOp(<,Id(a),BinaryOp(+,Id(b),Id(c))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,442))
    def test_dowhile_statement_3(self):
        input = """void main(string args[]){
            do{ 
                a+b=1;
                if(a>b) break;
                else return; 
            }
            {
                int x,y,z;
                x=y+z;
            }while a[a<b+c];
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([Dowhile([Block([BinaryOp(=,BinaryOp(+,Id(a),Id(b)),IntLiteral(1)),If(BinaryOp(>,Id(a),Id(b)),Break(),Return())]),Block([VarDecl(x,IntType),VarDecl(y,IntType),VarDecl(z,IntType),BinaryOp(=,Id(x),BinaryOp(+,Id(y),Id(z)))])],ArrayCell(Id(a),BinaryOp(<,Id(a),BinaryOp(+,Id(b),Id(c)))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,443))
    def test_dowhile_statement_4(self):
        input = """void main(string args[]){
            do{ 
                //void var;
                -a+c=d;
            }
            while a>2.4e3;
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([Dowhile([Block([BinaryOp(=,BinaryOp(+,UnaryOp(-,Id(a)),Id(c)),Id(d))])],BinaryOp(>,Id(a),FloatLiteral(2400.0)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,444))
    def test_dowhile_statement_5(self):
        input = """void main(string args[]){
            do{ 
                consolelog("string\\n");
                print(a,b,c);
                if(PPL==pass)
                    print("An mung");
            }
            while (PPL==pass);
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([Dowhile([Block([CallExpr(Id(consolelog),[StringLiteral(string\\n)]),CallExpr(Id(print),[Id(a),Id(b),Id(c)]),If(BinaryOp(==,Id(PPL),Id(pass)),CallExpr(Id(print),[StringLiteral(An mung)]))])],BinaryOp(==,Id(PPL),Id(pass)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,445))
    def test_dowhile_statement_6(self):
        input = """void main(string args[]){
            int i;
            i=0;
            do{ 
                dowhilebidao=true;
                return false;
                toPassPPL=true;
                i=i+1;
            }
            while (PPL==pass);
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,ArrayTypePointer(StringType))],VoidType,Block([VarDecl(i,IntType),BinaryOp(=,Id(i),IntLiteral(0)),Dowhile([Block([BinaryOp(=,Id(dowhilebidao),BooleanLiteral(true)),Return(BooleanLiteral(false)),BinaryOp(=,Id(toPassPPL),BooleanLiteral(true)),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])],BinaryOp(==,Id(PPL),Id(pass)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,446))

    #test break statement
    def test_break_statement(self):
        input = """float test(){
            break;
        }"""
        expect = "Program([FuncDecl(Id(test),[],FloatType,Block([Break()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,447))
    def test_break_statement_1(self):
        input = """float test(){
            if(a>b)
                break;
            else
                -a/b+c*1=d;
        }"""
        expect = "Program([FuncDecl(Id(test),[],FloatType,Block([If(BinaryOp(>,Id(a),Id(b)),Break(),BinaryOp(=,BinaryOp(+,BinaryOp(/,UnaryOp(-,Id(a)),Id(b)),BinaryOp(*,Id(c),IntLiteral(1))),Id(d)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,448))
    def test_break_statement_2(self):
        input = """float test(){
           for(i=1;i<10;i=i+1){
               a="Principle";
               b="Programming";
               c="Language";
               z=a+b+c;
               if(z==null) break;
               print("rs = " + z);
           }
        }"""
        expect = "Program([FuncDecl(Id(test),[],FloatType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,Id(a),StringLiteral(Principle)),BinaryOp(=,Id(b),StringLiteral(Programming)),BinaryOp(=,Id(c),StringLiteral(Language)),BinaryOp(=,Id(z),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c))),If(BinaryOp(==,Id(z),Id(null)),Break()),CallExpr(Id(print),[BinaryOp(+,StringLiteral(rs = ),Id(z))])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,449))
    
    #test continue statement
    def test_continue_statement(self):
        input = """float foo(){
                    if(true) continue;           
                }"""
        expect = "Program([FuncDecl(Id(foo),[],FloatType,Block([If(BooleanLiteral(true),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,450))
    def test_continue_statement_1(self):
        input = """float foo(){
                    do{
                        a=a+1;
                        if(a<0) continue;
                    }
                    while (a>10);
                    if(true) continue;           
                }"""
        expect = "Program([FuncDecl(Id(foo),[],FloatType,Block([Dowhile([Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1))),If(BinaryOp(<,Id(a),IntLiteral(0)),Continue())])],BinaryOp(>,Id(a),IntLiteral(10))),If(BooleanLiteral(true),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,451))
    def test_continue_statement_2(self):
        input = """int main(){
            cout((array[i])[j]);
            if(a>c) continue;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(cout),[ArrayCell(ArrayCell(Id(array),Id(i)),Id(j))]),If(BinaryOp(>,Id(a),Id(c)),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,452))
    def test_continue_statement_3(self):
        input = """int main(){
            do { 
                continue;
            }
            while((arr[i])[j]);
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([Continue()])],ArrayCell(ArrayCell(Id(arr),Id(i)),Id(j)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,453))

    #test return statement
    def test_return_statement(self):
        input = """float foo(int a,int b){
                    return a+b;          
                }"""
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,IntType)],FloatType,Block([Return(BinaryOp(+,Id(a),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,454))
    def test_return_statement_1(self):
        input = """float gt(int n){
                    if(n==1 || n==0) return 1;
                    return n*gt(n-1);          
                }"""
        expect = "Program([FuncDecl(Id(gt),[VarDecl(n,IntType)],FloatType,Block([If(BinaryOp(||,BinaryOp(==,Id(n),IntLiteral(1)),BinaryOp(==,Id(n),IntLiteral(0))),Return(IntLiteral(1))),Return(BinaryOp(*,Id(n),CallExpr(Id(gt),[BinaryOp(-,Id(n),IntLiteral(1))])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,455))
    def test_return_statement_2(self):
        input = """float gt(int n){
                    return a[a[a]];        
                }"""
        expect = "Program([FuncDecl(Id(gt),[VarDecl(n,IntType)],FloatType,Block([Return(ArrayCell(Id(a),ArrayCell(Id(a),Id(a))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,456))
    def test_return_statement_3(self):
        input = """float gt(int n){
                    return;
                }"""
        expect = "Program([FuncDecl(Id(gt),[VarDecl(n,IntType)],FloatType,Block([Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,457))
    def test_return_statement_4(self):
        input = """float gt(int n){
                    return a[a[a]]+b[i]==c;        
                }"""
        expect = "Program([FuncDecl(Id(gt),[VarDecl(n,IntType)],FloatType,Block([Return(BinaryOp(==,BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(a),Id(a))),ArrayCell(Id(b),Id(i))),Id(c)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,458))
    def test_return_statement_5(self):
        input = """int gt(int n){
                    if (a==b)
                        return a[a[a]]+b[i]==c;  
                    return null;      
                }"""
        expect = "Program([FuncDecl(Id(gt),[VarDecl(n,IntType)],IntType,Block([If(BinaryOp(==,Id(a),Id(b)),Return(BinaryOp(==,BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(a),Id(a))),ArrayCell(Id(b),Id(i))),Id(c)))),Return(Id(null))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,459))

    #test expression statement
    def test_expression_statement(self):
        input = """float gt(int n){
                    n=n*n;
                    n+2;
                    100;
                    1.E2;        
                }"""
        expect = "Program([FuncDecl(Id(gt),[VarDecl(n,IntType)],FloatType,Block([BinaryOp(=,Id(n),BinaryOp(*,Id(n),Id(n))),BinaryOp(+,Id(n),IntLiteral(2)),IntLiteral(100),FloatLiteral(100.0)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,460))
    def test_expression_statement_1(self):
        input = """float gt(int n){
                    n=n*n;
                    gt(100,n+2);
                    1.E2;        
                }"""
        expect = "Program([FuncDecl(Id(gt),[VarDecl(n,IntType)],FloatType,Block([BinaryOp(=,Id(n),BinaryOp(*,Id(n),Id(n))),CallExpr(Id(gt),[IntLiteral(100),BinaryOp(+,Id(n),IntLiteral(2))]),FloatLiteral(100.0)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,461))
    def test_expression_statement_2(self):
        input = """float gt(int n){
                    a[a[x=y+z]]=ab;
                    x2;     
                }"""
        expect = "Program([FuncDecl(Id(gt),[VarDecl(n,IntType)],FloatType,Block([BinaryOp(=,ArrayCell(Id(a),ArrayCell(Id(a),BinaryOp(=,Id(x),BinaryOp(+,Id(y),Id(z))))),Id(ab)),Id(x2)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,462))
    
    #test block statement
    def test_block_statement(self):
        input = """void main(string args){
                    {
                        a>b;
                        a=x*y/z;
                        x2;
                        a[4];
                    }    
                }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(args,StringType)],VoidType,Block([Block([BinaryOp(>,Id(a),Id(b)),BinaryOp(=,Id(a),BinaryOp(/,BinaryOp(*,Id(x),Id(y)),Id(z))),Id(x2),ArrayCell(Id(a),IntLiteral(4))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,463))
    def test_block_statement_1(self):
        input = """int main(){
            float a;
            a(10,a[a[7]],c+d>b);
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(a,FloatType),CallExpr(Id(a),[IntLiteral(10),ArrayCell(Id(a),ArrayCell(Id(a),IntLiteral(7))),BinaryOp(>,BinaryOp(+,Id(c),Id(d)),Id(b))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,464))
    def test_block_statement_2(self):
        input = """void func(){
            int a;
            i+i/u-5*7+"hello";
            a-a>=PPL-5;
            z*z+3;
        } """
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(+,BinaryOp(-,BinaryOp(+,Id(i),BinaryOp(/,Id(i),Id(u))),BinaryOp(*,IntLiteral(5),IntLiteral(7))),StringLiteral(hello)),BinaryOp(>=,BinaryOp(-,Id(a),Id(a)),BinaryOp(-,Id(PPL),IntLiteral(5))),BinaryOp(+,BinaryOp(*,Id(z),Id(z)),IntLiteral(3))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,465))
    def test_block_statement_3(self):
        input = """void func(){
            a=true;
            true+false=true;
            true*false=false;
        }"""
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([BinaryOp(=,Id(a),BooleanLiteral(true)),BinaryOp(=,BinaryOp(+,BooleanLiteral(true),BooleanLiteral(false)),BooleanLiteral(true)),BinaryOp(=,BinaryOp(*,BooleanLiteral(true),BooleanLiteral(false)),BooleanLiteral(false))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,466))
    def test_block_statement_4(self):
        input = """void func(){
            a=true;
            array[true+false]=true*false;
            b[true[false]]=false;
        }"""
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([BinaryOp(=,Id(a),BooleanLiteral(true)),BinaryOp(=,ArrayCell(Id(array),BinaryOp(+,BooleanLiteral(true),BooleanLiteral(false))),BinaryOp(*,BooleanLiteral(true),BooleanLiteral(false))),BinaryOp(=,ArrayCell(Id(b),ArrayCell(BooleanLiteral(true),BooleanLiteral(false))),BooleanLiteral(false))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,467))
    def test_block_statement_5(self):
        input = """void main(){
            int a[10];
            a[0]=false;
            a[1]=-true+6/a;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,ArrayType(IntType,10)),BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),BooleanLiteral(false)),BinaryOp(=,ArrayCell(Id(a),IntLiteral(1)),BinaryOp(+,UnaryOp(-,BooleanLiteral(true)),BinaryOp(/,IntLiteral(6),Id(a))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,468))
    def test_block_statement_6(self):
        input = """void func(){
            true;
            false;
        }"""
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([BooleanLiteral(true),BooleanLiteral(false)]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,469))
    def test_block_statement_7(self):
        input = """void main(){
            boolean a,b;
            a=false;
            b=true;
            do{
                a+b;
                int i;
                for(i=0;i<10;i=i+1)
                    print("PPL is passed");
            }while a==true && b==false;
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,BoolType),VarDecl(b,BoolType),BinaryOp(=,Id(a),BooleanLiteral(false)),BinaryOp(=,Id(b),BooleanLiteral(true)),Dowhile([Block([BinaryOp(+,Id(a),Id(b)),VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));CallExpr(Id(print),[StringLiteral(PPL is passed)]))])],BinaryOp(&&,BinaryOp(==,Id(a),BooleanLiteral(true)),BinaryOp(==,Id(b),BooleanLiteral(false))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,470))
    def test_block_statement_more_for(self):
        input = """void main(){
            for (a=1;a<10;a=a*2){
                for(b=2;b==10;b=b*2){
                    int a;
                    string b;
                    b = a + 1;
                }
            }
            for(d=1;d!=1;d=d+1){
                int e;
                e = d;
            }
            for(c=100;c!=0;c=c%2){
                for(d=1000;d>0;d=d%10){
                    int e;
                    e = d;
                    string d;
                    d = e;
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([VarDecl(a,IntType),VarDecl(b,StringType),BinaryOp(=,Id(b),BinaryOp(+,Id(a),IntLiteral(1)))]))])),For(BinaryOp(=,Id(d),IntLiteral(1));BinaryOp(!=,Id(d),IntLiteral(1));BinaryOp(=,Id(d),BinaryOp(+,Id(d),IntLiteral(1)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d))])),For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(e))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,471))
    def test_block_statement_more_for_1(self):
        input = """void main(){
            for (a=1;a<10;a=a*2){
                for(b=2;b==10;b=b*2){
                    for(c=100;c!=0;c=c%2){
                        for(d=1000;d>0;d=d%10){
                            int e;
                            e = d;
                            string d;
                            d = e;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(*,Id(a),IntLiteral(2)));Block([For(BinaryOp(=,Id(b),IntLiteral(2));BinaryOp(==,Id(b),IntLiteral(10));BinaryOp(=,Id(b),BinaryOp(*,Id(b),IntLiteral(2)));Block([For(BinaryOp(=,Id(c),IntLiteral(100));BinaryOp(!=,Id(c),IntLiteral(0));BinaryOp(=,Id(c),BinaryOp(%,Id(c),IntLiteral(2)));Block([For(BinaryOp(=,Id(d),IntLiteral(1000));BinaryOp(>,Id(d),IntLiteral(0));BinaryOp(=,Id(d),BinaryOp(%,Id(d),IntLiteral(10)));Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(d)),VarDecl(d,StringType),BinaryOp(=,Id(d),Id(e))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,472))
    def test_block_statement_more_if(self):
        input = """void main(){
            int a;
            a = true;
            if (true){
                if (a == true){
                    if (!a){
                        a = false;
                        string b;
                        b = a;
                        if (b){
                            boolean c;
                            c = b;
                            if (!c){
                                return;
                            }
                            else{
                                if (d && !e){
                                    string t;
                                    t = d;
                                }
                            }
                        }
                    }
                    else{
                        if ((a == b || c != b) && a > b){
                            int e;
                            e = a;
                        }
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,IntType),BinaryOp(=,Id(a),BooleanLiteral(true)),If(BooleanLiteral(true),Block([If(BinaryOp(==,Id(a),BooleanLiteral(true)),Block([If(UnaryOp(!,Id(a)),Block([BinaryOp(=,Id(a),BooleanLiteral(false)),VarDecl(b,StringType),BinaryOp(=,Id(b),Id(a)),If(Id(b),Block([VarDecl(c,BoolType),BinaryOp(=,Id(c),Id(b)),If(UnaryOp(!,Id(c)),Block([Return()]),Block([If(BinaryOp(&&,Id(d),UnaryOp(!,Id(e))),Block([VarDecl(t,StringType),BinaryOp(=,Id(t),Id(d))]))]))]))]),Block([If(BinaryOp(&&,BinaryOp(||,BinaryOp(==,Id(a),Id(b)),BinaryOp(!=,Id(c),Id(b))),BinaryOp(>,Id(a),Id(b))),Block([VarDecl(e,IntType),BinaryOp(=,Id(e),Id(a))]))]))]))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,473))

    #test more complex call expression
    def test_more_complex_call_expression(self):
        input = """
        string print(string a){
            print(a);
        }
        int[] map(int list[]){
            int i;
            for(i=0;i<length(list);i=i+1){
                list[i]=(list[i]*2+1)/3;
            }
            int newlist[10];
            newlist=list;
            return newlist;
        }
        void main(){
            int a[10],b[10];
            b=map(a);
            print(print(print(print(map(b(map(a)))))));
        }"""
        expect = "Program([FuncDecl(Id(print),[VarDecl(a,StringType)],StringType,Block([CallExpr(Id(print),[Id(a)])])),FuncDecl(Id(map),[VarDecl(list,ArrayTypePointer(IntType))],ArrayTypePointer(IntType),Block([VarDecl(i,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),CallExpr(Id(length),[Id(list)]));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([BinaryOp(=,ArrayCell(Id(list),Id(i)),BinaryOp(/,BinaryOp(+,BinaryOp(*,ArrayCell(Id(list),Id(i)),IntLiteral(2)),IntLiteral(1)),IntLiteral(3)))])),VarDecl(newlist,ArrayType(IntType,10)),BinaryOp(=,Id(newlist),Id(list)),Return(Id(newlist))])),FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,ArrayType(IntType,10)),VarDecl(b,ArrayType(IntType,10)),BinaryOp(=,Id(b),CallExpr(Id(map),[Id(a)])),CallExpr(Id(print),[CallExpr(Id(print),[CallExpr(Id(print),[CallExpr(Id(print),[CallExpr(Id(map),[CallExpr(Id(b),[CallExpr(Id(map),[Id(a)])])])])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,474))
    def test_more_complex_call_expression_1(self):
        input = """
        string print(string a){
            print(a);
        }
        void main(){
            int a[10],b[10];
            b=map(a);
            reduce(lambda(x,x*x),a,b[0]);
            print(print(print(print(map(b(map(a)))))));
            reduce(map(a,reduce(b,map(a))));
        }"""
        expect = "Program([FuncDecl(Id(print),[VarDecl(a,StringType)],StringType,Block([CallExpr(Id(print),[Id(a)])])),FuncDecl(Id(main),[],VoidType,Block([VarDecl(a,ArrayType(IntType,10)),VarDecl(b,ArrayType(IntType,10)),BinaryOp(=,Id(b),CallExpr(Id(map),[Id(a)])),CallExpr(Id(reduce),[CallExpr(Id(lambda),[Id(x),BinaryOp(*,Id(x),Id(x))]),Id(a),ArrayCell(Id(b),IntLiteral(0))]),CallExpr(Id(print),[CallExpr(Id(print),[CallExpr(Id(print),[CallExpr(Id(print),[CallExpr(Id(map),[CallExpr(Id(b),[CallExpr(Id(map),[Id(a)])])])])])])]),CallExpr(Id(reduce),[CallExpr(Id(map),[Id(a),CallExpr(Id(reduce),[Id(b),CallExpr(Id(map),[Id(a)])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,475))

    #test some complex expression
    def test_complex_expression(self):
        input = """void func(){
            true+false>(true*false+PPL(hello,false,PPL[foo(10,20)]));
        }"""
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([BinaryOp(>,BinaryOp(+,BooleanLiteral(true),BooleanLiteral(false)),BinaryOp(+,BinaryOp(*,BooleanLiteral(true),BooleanLiteral(false)),CallExpr(Id(PPL),[Id(hello),BooleanLiteral(false),ArrayCell(Id(PPL),CallExpr(Id(foo),[IntLiteral(10),IntLiteral(20)]))])))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,476))
    def test_complex_expression_1(self):
        input = """void func(){
            complex=(((((((x/2)))))))/n;
        }"""
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([BinaryOp(=,Id(complex),BinaryOp(/,BinaryOp(/,Id(x),IntLiteral(2)),Id(n)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,477))
    def test_complex_expression_2(self):
        input = """void func(){
            complex=complex(x(x(x(x(x(x(x/2)))))))/n;
        }"""
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([BinaryOp(=,Id(complex),BinaryOp(/,CallExpr(Id(complex),[CallExpr(Id(x),[CallExpr(Id(x),[CallExpr(Id(x),[CallExpr(Id(x),[CallExpr(Id(x),[CallExpr(Id(x),[BinaryOp(/,Id(x),IntLiteral(2))])])])])])])]),Id(n)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,478))
    def test_complex_expression_3(self):
        input = """void func(){
            {
                a=a+1/x*3;
                {
                    a=a+1/x*3;
                    {
                        a=a+1/x*3;
                    }
                }
            }
        }"""
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),BinaryOp(*,BinaryOp(/,IntLiteral(1),Id(x)),IntLiteral(3)))),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),BinaryOp(*,BinaryOp(/,IntLiteral(1),Id(x)),IntLiteral(3)))),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),BinaryOp(*,BinaryOp(/,IntLiteral(1),Id(x)),IntLiteral(3))))])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,479))
    def test_complex_expression_4(self):
        input = """void func(){
            {
                int mark;
                result(mark);
                if(mark<5)
                    println("Trung binh");
                else if (5<=mark&&mark<8)
                    println("Kha");
                else
                    println("Gioi");  
            }
        }"""
        expect = "Program([FuncDecl(Id(func),[],VoidType,Block([Block([VarDecl(mark,IntType),CallExpr(Id(result),[Id(mark)]),If(BinaryOp(<,Id(mark),IntLiteral(5)),CallExpr(Id(println),[StringLiteral(Trung binh)]),If(BinaryOp(&&,BinaryOp(<=,IntLiteral(5),Id(mark)),BinaryOp(<,Id(mark),IntLiteral(8))),CallExpr(Id(println),[StringLiteral(Kha)]),CallExpr(Id(println),[StringLiteral(Gioi)])))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,480))
    def test_complex_expression_5(self):
        input = """void main(){
            int oddSum, evenSum,arr[10],i;
            oddSum = evenSum =0;
            for(i=0;i<10;i=i+1)
                arr[i]=i;
            for(i=0;i<10;i=i+1){
                if(arr[i]%2==0)
                    evenSum = evenSum + arr[i];
                else
                    oddSum = oddSum + arr[i];
            }        
        }"""
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([VarDecl(oddSum,IntType),VarDecl(evenSum,IntType),VarDecl(arr,ArrayType(IntType,10)),VarDecl(i,IntType),BinaryOp(=,Id(oddSum),BinaryOp(=,Id(evenSum),IntLiteral(0))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,ArrayCell(Id(arr),Id(i)),Id(i))),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(arr),Id(i)),IntLiteral(2)),IntLiteral(0)),BinaryOp(=,Id(evenSum),BinaryOp(+,Id(evenSum),ArrayCell(Id(arr),Id(i)))),BinaryOp(=,Id(oddSum),BinaryOp(+,Id(oddSum),ArrayCell(Id(arr),Id(i)))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,481))
    def test_complex_expression_6(self):
        input = """int foo () {
            if (a+1) {
                {
                    {
                        {
                            if(b+a) foo();
                        }
                    }
                }
            } 
            else {
                if (c+d) t+a; 
                else 
                func(a(b(c)))[f+6*d()];
            }
        }"""
        expect = "Program([FuncDecl(Id(foo),[],IntType,Block([If(BinaryOp(+,Id(a),IntLiteral(1)),Block([Block([Block([Block([If(BinaryOp(+,Id(b),Id(a)),CallExpr(Id(foo),[]))])])])]),Block([If(BinaryOp(+,Id(c),Id(d)),BinaryOp(+,Id(t),Id(a)),ArrayCell(CallExpr(Id(func),[CallExpr(Id(a),[CallExpr(Id(b),[Id(c)])])]),BinaryOp(+,Id(f),BinaryOp(*,IntLiteral(6),CallExpr(Id(d),[])))))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,482))
    def test_complex_expression_7(self):
        input = """int main () {
            putIntLn(4);
            ar[12];
            foo(a[10],r);
            break;continue;
        }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(putIntLn),[IntLiteral(4)]),ArrayCell(Id(ar),IntLiteral(12)),CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(10)),Id(r)]),Break(),Continue()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,483))
    def test_complex_expression_8(self):
        input = """void f(int a,float b, float c){
            true && false || (2 > 3/5);
        }"""
        expect = "Program([FuncDecl(Id(f),[VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,FloatType)],VoidType,Block([BinaryOp(||,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)),BinaryOp(>,IntLiteral(2),BinaryOp(/,IntLiteral(3),IntLiteral(5))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,484))
    def test_complex_expression_9(self):
        input = """void f(int a,float b, float c){
            true && false && (2 > 3/5);
            print(print("Hello word"));
        }"""
        expect = "Program([FuncDecl(Id(f),[VarDecl(a,IntType),VarDecl(b,FloatType),VarDecl(c,FloatType)],VoidType,Block([BinaryOp(&&,BinaryOp(&&,BooleanLiteral(true),BooleanLiteral(false)),BinaryOp(>,IntLiteral(2),BinaryOp(/,IntLiteral(3),IntLiteral(5)))),CallExpr(Id(print),[CallExpr(Id(print),[StringLiteral(Hello word)])])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,485))

    #test more complex vardecl
    def test_complex_vardecl(self):
        input = """int a,b,a[10],b[10],c;
        string c,f,e,d,g[10];
        float b,l,k,j;
        boolean hello,program;"""
        expect = "Program([VarDecl(a,IntType),VarDecl(b,IntType),VarDecl(a,ArrayType(IntType,10)),VarDecl(b,ArrayType(IntType,10)),VarDecl(c,IntType),VarDecl(c,StringType),VarDecl(f,StringType),VarDecl(e,StringType),VarDecl(d,StringType),VarDecl(g,ArrayType(StringType,10)),VarDecl(b,FloatType),VarDecl(l,FloatType),VarDecl(k,FloatType),VarDecl(j,FloatType),VarDecl(hello,BoolType),VarDecl(program,BoolType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,486))

    #test more complex funcdecl
    def test_complex_funcdecl(self):
        input = """int[] map(int list[]){}
        int[] reduce(int a[],int list){}
        float hello(float hello){}
        int start,end,list[10];"""
        expect = "Program([FuncDecl(Id(map),[VarDecl(list,ArrayTypePointer(IntType))],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(reduce),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(list,IntType)],ArrayTypePointer(IntType),Block([])),FuncDecl(Id(hello),[VarDecl(hello,FloatType)],FloatType,Block([])),VarDecl(start,IntType),VarDecl(end,IntType),VarDecl(list,ArrayType(IntType,10))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,487))
    def test_complex_funcdecl_1(self):
        input = """int[] map(int list[]){
            a=a+1;
        }
        int[] reduce(int a[],int list){
            b=b+1;
        }
        float hello(float hello){
            c=c+1;
        }
        """
        expect = "Program([FuncDecl(Id(map),[VarDecl(list,ArrayTypePointer(IntType))],ArrayTypePointer(IntType),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])),FuncDecl(Id(reduce),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(list,IntType)],ArrayTypePointer(IntType),Block([BinaryOp(=,Id(b),BinaryOp(+,Id(b),IntLiteral(1)))])),FuncDecl(Id(hello),[VarDecl(hello,FloatType)],FloatType,Block([BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,488))
    def test_complex_funcdecl_2(self):
        input = """int[] map(int list[]){
            a=a+1;
        }
        int[] reduce(int a[],int list){
            (foo()[10])[10];
        }
        float hello(float hello){
            array(array()[10]);
        }
        """
        expect = "Program([FuncDecl(Id(map),[VarDecl(list,ArrayTypePointer(IntType))],ArrayTypePointer(IntType),Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)))])),FuncDecl(Id(reduce),[VarDecl(a,ArrayTypePointer(IntType)),VarDecl(list,IntType)],ArrayTypePointer(IntType),Block([ArrayCell(ArrayCell(CallExpr(Id(foo),[]),IntLiteral(10)),IntLiteral(10))])),FuncDecl(Id(hello),[VarDecl(hello,FloatType)],FloatType,Block([CallExpr(Id(array),[ArrayCell(CallExpr(Id(array),[]),IntLiteral(10))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,489))
    
    #test for nested
    def test_for_nested(self):
        input = """int main(){
            for(i=0;i<10;i=i+1){
                {
                    {
                        for(j=0;j<10;j=j+1){
                            {
                                {
                                    print("End");
                                }
                            }
                        }
                    }
                }
            }
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([Block([Block([For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<,Id(j),IntLiteral(10));BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)));Block([Block([Block([CallExpr(Id(print),[StringLiteral(End)])])])]))])])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,490))

    #test dowhile nested
    def test_dowhile_nested(self):
        input = """int main(){
            do{
                do{
                    do{
                        do{
                            print("End");
                        } while true;
                    }while true;
                }while true;
            }while true;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([Dowhile([Block([Dowhile([Block([Dowhile([Block([CallExpr(Id(print),[StringLiteral(End)])])],BooleanLiteral(true))])],BooleanLiteral(true))])],BooleanLiteral(true))])],BooleanLiteral(true))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,491))

    #test arraycell nested
    def test_arraycell_nested(self):
        input = """int main(){
            arraycell[arraycell[arraycell[arraycell[arraycell[10]]]]];
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(Id(arraycell),ArrayCell(Id(arraycell),ArrayCell(Id(arraycell),ArrayCell(Id(arraycell),ArrayCell(Id(arraycell),IntLiteral(10))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,492))
    def test_arraycell_nested_1(self):
        input = """int main(){
            arraycell()[arraycell()[arraycell()[arraycell()[arraycell()[10]]]]];
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(CallExpr(Id(arraycell),[]),ArrayCell(CallExpr(Id(arraycell),[]),ArrayCell(CallExpr(Id(arraycell),[]),ArrayCell(CallExpr(Id(arraycell),[]),ArrayCell(CallExpr(Id(arraycell),[]),IntLiteral(10))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,493))
    def test_arraycell_nested_2(self):
        input = """int main(){
            arraycell(1,2,a)[arraycell(c,d)[arraycell()[arraycell()[arraycell(e,f)[10]]]]];
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(CallExpr(Id(arraycell),[IntLiteral(1),IntLiteral(2),Id(a)]),ArrayCell(CallExpr(Id(arraycell),[Id(c),Id(d)]),ArrayCell(CallExpr(Id(arraycell),[]),ArrayCell(CallExpr(Id(arraycell),[]),ArrayCell(CallExpr(Id(arraycell),[Id(e),Id(f)]),IntLiteral(10))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,494))
    def test_arraycell_nested_3(self):
        input = """int main(){
            arraycell(1,2,a)[arraycell(c,d)[arraycell(e,f)[arraycell(g)[arraycell(e,f)[10+k]]]]];
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([ArrayCell(CallExpr(Id(arraycell),[IntLiteral(1),IntLiteral(2),Id(a)]),ArrayCell(CallExpr(Id(arraycell),[Id(c),Id(d)]),ArrayCell(CallExpr(Id(arraycell),[Id(e),Id(f)]),ArrayCell(CallExpr(Id(arraycell),[Id(g)]),ArrayCell(CallExpr(Id(arraycell),[Id(e),Id(f)]),BinaryOp(+,IntLiteral(10),Id(k)))))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,495))

    #test simple program
    def test_simple_program(self):
        input = """void main() {(5+x)[a];}
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(BinaryOp(+,IntLiteral(5),Id(x)),Id(a))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,496))
    def test_simple_program_1(self):
        input = """void main() {a[pow(2,3)];}
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(a),CallExpr(Id(pow),[IntLiteral(2),IntLiteral(3)]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,497))
    def test_simple_program_2(self):
        input = """void main() {maxarray[pow(10,10)[10]];}
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(maxarray),ArrayCell(CallExpr(Id(pow),[IntLiteral(10),IntLiteral(10)]),IntLiteral(10)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,498))
    def test_simple_program_3(self):
        input = """void main() {
            maxarray[pow(10,10)[10]];
            print("End test case");
            }
        """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([ArrayCell(Id(maxarray),ArrayCell(CallExpr(Id(pow),[IntLiteral(10),IntLiteral(10)]),IntLiteral(10))),CallExpr(Id(print),[StringLiteral(End test case)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,499))