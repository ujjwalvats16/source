#[derive(Debug)]

enum exam{
    pass(i32),
    fail(i32)
}

impl exam{
    fn display_value(&self){
        if let &exam::pass(value)=self{
            println!("value of pass mark is {}",value);


        }
    }


}

fn main(){

    let exam_1=exam::pass(70);
    exam_1.display_value();
}