import { AuthGuard } from './auth/auth-guard.service';
import { MainComponent } from './main/main.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';



const routes: Routes = [
  {path: '', component: MainComponent, canActivate: [ AuthGuard ]},
  {path:'accounts', children: [
    {path: 'register', component: RegisterComponent},
    {path: 'login', component: LoginComponent},
  ]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
