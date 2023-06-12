public class SessionServiceAPI {
    private SessionService sessionService;

    public SessionServiceAPI(SessionService sessionService) {
        this.sessionService = sessionService;
    }

    @GET
    @Path("/session")
    public Response getSession(@HeaderParam("Session-Token") String sessionToken) {
        String userId = sessionService.getUserIdFromSession(sessionToken);
        if (userId != null) {
            return Response.ok(userId).build();
        } else {
            return Response.status(Response.Status.UNAUTHORIZED).build();
        }
    }
}