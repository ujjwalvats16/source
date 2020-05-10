
//simple enum with variant name
enum Exam{
    pass,
    fail,
}

fn main(){
    let first_exam=Exam::fail;
    let second_exam=Exam::pass;
    display_exam(first_exam);
    display_exam(second_exam);


}

fn display_exam(f_e:Exam){
    println!("{:?}",f_e);
}

//enum with variant value
#[derive(Debug)]
enum Exam{
    pass(i32,i32,i32),
    fail(String),
}

fn main(){
    let first_exam=Exam::fail("partial_fail".to_string());
    let second_exam=Exam::pass(100,120,150);
    display_exam(first_exam);
    display_exam(second_exam);


}

fn display_exam(f_e:Exam){
    println!("{:?}",f_e);
}