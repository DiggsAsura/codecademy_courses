use axum::{
    routing::{get, post, get_service},
    http::StatusCode,
    response::IntoResponse,
    Json, Router};

use axum::extract::Path;
use tower_http::services::ServeFile;

use std::net::SocketAddr;
use serde::{Deserialize, Serialize};
use serde_json::{json};

use std::{io};



#[derive(Deserialize)]
struct CreateUser {
    username: String,
}

#[derive(Debug, Serialize,Deserialize, Clone, Eq, Hash, PartialEq)]
struct User {
    id: u64,
    username: String,
}

#[tokio::main]
async fn main() {

    tracing_subscriber::fmt::init();
    let app = Router::new()
        .route("/", get(root))
        .route("/user", post(create_user))
        .route("/hello/:name", get(json_hello))
        .route("/static", get_service(ServeFile::new("static/hello.html"))
            .handle_error(|error: io::Error| async move {
                (
                    StatusCode::INTERNAL_SERVER_ERROR,
                    format!("Unhandled internal error: {}", error),
                )
            }));

    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    tracing::info!("listening on {}", addr);
    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();


}

async fn root() -> &'static str {
    "Hello, World!"
}

async fn create_user(Json(payload): Json<CreateUser>) -> impl IntoResponse {
    let user = User {
        id: 1337,
        username: payload.username
    };

    (StatusCode::CREATED, Json(user))
}


async fn json_hello(Path(name): Path<String>) -> impl IntoResponse {
    let greeting = name.as_str();
    let hello = String::from("Hello ");

    (StatusCode::OK, Json(json!({"message": hello + greeting })))
}

