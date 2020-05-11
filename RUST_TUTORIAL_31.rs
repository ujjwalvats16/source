#[derive(Debug)]
enum exam{
    pass(i32),
    fail(i32),
}
impl exam{
    fn display(&self){

        if let &exam::fail(value)=self{
            println!("value of the variant is {}",value);
        }
        else{
            println!(" not failed case with {:?}",self);
        }
    }
}



fn main(){

let exam_1=exam::pass(70);
let exam_2=exam::fail(50);
exam_1.display();
exam_2.display();

}