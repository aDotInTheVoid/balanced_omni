export interface AuthState {
    user: User | null
    isLogedIn: Boolean,
    errors: any
}

export interface User {
    email: string,
    username: string,
    token: string,
}

export interface LoginCredentials{
    email: String,
    password: String
}
