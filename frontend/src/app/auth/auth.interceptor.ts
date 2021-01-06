import { HttpErrorResponse, HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from "@angular/common/http";
import { Observable, throwError } from "rxjs";
import { catchError } from "rxjs/operators";


export class AuthInterceptor implements HttpInterceptor{


  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    let token = localStorage.getItem('token')
    if(token){
      const authReq = req.clone(
        {
          setHeaders: {
            Authorization: `token ${token}`
          }
        }
      )
      return next.handle(authReq)
      .pipe(catchError((error)=>{
        if(error instanceof HttpErrorResponse){
          if(error.status === 401){
            localStorage.removeItem('token')
          }
        }
        return throwError(error)
      }))
    }
    return next.handle(req);
  }

}
