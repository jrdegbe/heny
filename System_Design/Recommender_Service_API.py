public class RecommenderServiceAPI {
    private RecommenderService RecommenderService;

    public RecommenderServiceAPI(RecommenderService RecommenderService) {
        this.RecommenderService = RecommenderService;
    }

    @GET
    @Path("/matches/{userId}")
    public Response getMatches(@PathParam("userId") String userId) {
        List<Match> matches = RecommenderService.getMatches(userId);
        return Response.ok(matches).build();
    }
}