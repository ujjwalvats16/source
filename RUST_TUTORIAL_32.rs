#[derive(Debug)]
enum exam{
    pass(i32),
    fail(i32)
}
impl exam{
    fn return_func(&self)->i32{

        if let &exam::pass(value)=self{
            value
        }
        else{
            panic!("call on exam::pass() is failed on {:?}",self);
        }

    }
}


fn main(){
    let exam_1=exam::fail(70);
    let x=exam_1.return_func();
    println!("value of the passed mark is {}",x);
}