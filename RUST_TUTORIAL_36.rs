enum exam{
    pass(i32),
    fail(i32,)
}
impl exam{
    fn display(&self){
        match *self{
            exam::pass(value)=>println!("value is {}",value),
            exam::fail(value)=>println!("value is {}",value)

        }
    }
}

fn main(){
    let exam_1=exam::pass(70);
    exam_1.display();
}