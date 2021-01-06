import { AuthService } from './../auth.service';
import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { MatSnackBar, MatSnackBarConfig } from '@angular/material/snack-bar';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password1: ['', [Validators.required, Validators.minLength(8)]],
  })

  constructor(
    private fb: FormBuilder,
    private snackBar: MatSnackBar,
    private router: Router,
    private authService: AuthService
    ) { }

  ngOnInit(): void {
  }

  submit(): void{
    this.authService.login(this.loginForm.value).subscribe(
      (response) => {
        this.success()
      },
      (error) => {
        let message = ''
        if(error.status === 400){
          if(error.error.non_field_errors){
            message = 'Email ou senha incorretos'
          }
        } else if(error.status === 500){
          message = 'Erro interno no sistema, por favor tente mais tarde!'
        }
        this.errorHandler(message)
      }
    )
    this.clear()
  }

  clear(): void{
    this.loginForm.reset()
  }

  errorHandler(error: string){
    let config = new MatSnackBarConfig()
    config.duration = 4000
    this.snackBar.open(error, '', config)
  }

  success(): void{
    let config = new MatSnackBarConfig()
    config.duration = 4000
    const message = 'Login realizado com sucesso'
    this.snackBar.open(message, '', config)
    this.router.navigate([''])
  }

}
