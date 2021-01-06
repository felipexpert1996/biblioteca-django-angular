import { MatSnackBar, MatSnackBarConfig } from '@angular/material/snack-bar';
import { Observable } from 'rxjs';
import { AuthService } from './auth/auth.service';
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  authenticated$: Observable<boolean> = new Observable;

  constructor(private authService: AuthService, private snackBar: MatSnackBar){
    this.authenticated$ = this.authService.isAuthenticated();
  }

  logout(): void {
    let config = new MatSnackBarConfig()
    config.duration = 4000
    const message = 'Logout realizado com sucesso'
    this.snackBar.open(message, '', config)
    this.authService.logout().subscribe()
  }
}
