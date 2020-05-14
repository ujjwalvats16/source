use std::io;
#[derive(Debug)]

enum exam{
    pass(i32),
    fail(i32),
}

impl exam{
    fn validate_marks(&self,mark_ch:i32){
        if let &exam::pass(value)=self{
            let x:bool=value>mark_ch;
            if x{
                println!("you are eligible for scholsrship");
            }
            else{
                println!("you are not eligible for scholsrship");
            }
        }
        if let &exam::fail(value)=self{
            let x:i32=40-value;
            if x<10{
                println!("you are fligible to retake the eaxm with specific subject");
            }
            else{
                println!("you are not eligible for retake");
            }
        }
    }
}

fn main(){
let mark:i32=80;
println!("enter pass if you passed else enter fail");
let mut result=String::new();
io::stdin().read_line(&mut result).expect("error occured");
if result.trim()=="pass"{
    println!("enter the score you got");
let mut score_pass=String::new();
io::stdin().read_line(&mut score_pass).expect("error occured");

    let exam_1=exam::pass(score_pass.trim().parse::<i32>().unwrap());
    //println!("{:?}",exam_1);
    exam_1.validate_marks(mark);

}
else if result.trim()=="fail"{
println!("enter the score you got");
let mut score_fail=String::new();
io::stdin().read_line(&mut score_fail).expect("error occured");

    let exam_2=exam::fail(score_fail.trim().parse::<i32>().unwrap());
    exam_2.validate_marks(mark);
    
    //println!("{:?}",exam_2);

}
else{
    println!("invalid input")
}

}