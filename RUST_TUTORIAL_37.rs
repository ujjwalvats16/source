enum exam{
    pass(i32),
    fail(i32)
}
impl exam{
    fn get_value(&self)->i32{
        match *self{
            exam::pass(value)=>value,
            exam::fail(value)=>value
        }
    }
}
fn main(){
    let exam_1=exam::pass(70);
    let exam_2=exam::fail(50);
    let x=exam_1.get_value();
    println!("pass value is {}",x);
    let y=exam_2.get_value();
    println!("fail value is {}",y);
}