public class ProfileServiceAPI {
    private ProfileService profileService;

    public ProfileServiceAPI(ProfileService profileService) {
        this.profileService = profileService;
    }

    @POST
    @Path("/signup")
    public Response signUp(@FormParam("userId") String userId,
                           @FormParam("username") String username,
                           @FormParam("password") String password) {
        profileService.signUp(userId, username, password);
        return Response.status(Response.Status.CREATED).build();
    }

    @POST
    @Path("/login")
    public Response login(@FormParam("username") String username,
                          @FormParam("password") String password) {
        UserProfile userProfile = profileService.login(username, password);
        if (userProfile != null) {
            String sessionToken = sessionService.createSession(userProfile.getUserId());
            return Response.ok().header("Session-Token", sessionToken).build();
        } else {
            return Response.status(Response.Status.UNAUTHORIZED).build();
        }
    }
}