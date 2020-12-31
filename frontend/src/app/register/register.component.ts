import { RegisterService } from './register.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  registerForm = this.fb.group({
    username: ['', [Validators.required, Validators.minLength(5)]],
    email: ['', [Validators.required, Validators.email]],
    password1: ['', [Validators.required, Validators.minLength(8)]],
    password2: ['', [Validators.required, Validators.minLength(8)]],
  }, {
    validator: this.ConfirmedValidator('password1', 'password2')
  })

  constructor(private fb: FormBuilder, private registerService: RegisterService) { }

  ngOnInit(): void {
  }

  submit(): void{
    this.registerService.register(this.registerForm.value).subscribe(
      (value) => {console.log(value)}
    )
  }

  clear(): void{
    this.registerForm.reset()
  }

  ConfirmedValidator(controlName: string, matchingControlName: string){
    return (formGroup: FormGroup) => {
        const control = formGroup.controls[controlName];
        const matchingControl = formGroup.controls[matchingControlName];
        if (matchingControl.errors && !matchingControl.errors.confirmedvalidator) {
            return;
        }
        if (control.value !== matchingControl.value) {
            matchingControl.setErrors({ confirmedvalidator: true });
        } else {
            matchingControl.setErrors(null);
        }
    }
}

}
