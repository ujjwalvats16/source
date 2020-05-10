#[derive(Debug)]
enum exam{
    pass(i32),
    fail(i32),
    sub{english:i32,history:i32}
}

fn main(){

    let exam_1=exam::sub{english:60,history:65};
    display_enum(exam_1);

}

fn display_enum(ex:exam){
    println!("{:?}",ex);
}