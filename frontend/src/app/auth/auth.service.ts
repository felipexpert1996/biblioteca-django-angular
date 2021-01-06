import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, ReplaySubject } from 'rxjs';
import { Injectable } from '@angular/core';
import { tap } from 'rxjs/operators'
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private subjLoggedIn$: ReplaySubject<any> = new ReplaySubject(1);

  constructor(private http: HttpClient, private router: Router) { }

  register(user: User): Observable<any>{
    return this.http.post(`${environment.baseUrl}/account/registration/`, user)
  }

  login(user: User): Observable<any>{
    let u = {
      email: user.email,
      password: user.password1
    }
    return this.http.post(`${environment.baseUrl}/account/login/`, u).pipe(
      tap((us: any) => {
        localStorage.setItem('token', us.key);
        localStorage.setItem('email', u.email);
        this.subjLoggedIn$.next(true);
      })
    )
  }

  isAuthenticated(): Observable<any>{
    const token = localStorage.getItem('token')
    const email = localStorage.getItem('email')
    if(token && email){
      this.http.get<any>(`${environment.baseUrl}/account/verify/?email=${email}`).subscribe((response)=>{
        this.subjLoggedIn$.next(response['valid'])
      })
      return this.subjLoggedIn$.asObservable()
    } else {
      this.subjLoggedIn$.next(false)
      return this.subjLoggedIn$.asObservable()
    }
  }

  logout(): Observable<any>{
    return this.http.post(`${environment.baseUrl}/account/logout/`, {})
    .pipe(
      tap(()=> {
        localStorage.removeItem('token')
        localStorage.removeItem('email')
        this.subjLoggedIn$.next(false)
        this.router.navigate(['/accounts/login/'])
      })
    )
  }
}
