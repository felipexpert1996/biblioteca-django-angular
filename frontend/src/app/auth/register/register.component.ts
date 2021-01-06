import { AuthService } from './../auth.service';

import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatSnackBar, MatSnackBarConfig } from '@angular/material/snack-bar';
import { Router } from '@angular/router';

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

  constructor(
    private fb: FormBuilder,
    private registerService: AuthService,
    private snackBar: MatSnackBar,
    private router: Router) { }

  ngOnInit(): void {
  }

  submit(): void{
    this.registerService.register(this.registerForm.value).subscribe(
      (value) => {this.sucess()},
      (error) => {
        let message = ''
        if(error.status === 400){
          if(error.error.username && error.error.email){
            message = 'Nome de usuário e email já cadastrados'
          } else if(error.error.username){
            message = 'Nome de usuário já cadastrado'
          } else if(error.error.email){
            message = 'Email já cadastrado'
          }
        } else if(error.status === 500){
          message = 'Erro interno no sistema, por favor tente mais tarde!'
        }
        this.errorHandler(message)
      }
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

  errorHandler(error: string){
    let config = new MatSnackBarConfig()
    config.duration = 4000
    this.snackBar.open(error, '', config)
  }

  sucess(){
    let config = new MatSnackBarConfig()
    config.duration = 4000
    const message = 'Usuário cadastrado com sucesso realize o login para prosseguir'
    this.snackBar.open(message, '', config)
    this.router.navigate(['accounts/login'])
  }

}
